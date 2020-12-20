import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import csv
import time


IMAGE_PATH = os.path.abspath('../data/images/')
COORDINATES_PATH = os.path.abspath("../data/coord.csv")
KEY_PATH = os.path.abspath("./googleKey.secret")
URL = 'https://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom={}&size={}x{}&maptype=satellite&key={}'


def loadSaveImage(coords, number, zoom, satellite=True, size=640):
    saveName = '{}_{}_satellite' if satellite else '{}_{}_map'
    saveName = saveName.format(number, zoom)
    savePath = os.path.join(IMAGE_PATH, saveName)
    with open(KEY_PATH, 'r') as myfile:
        key = myfile.read()

    print("retrieving image {}...".format(number))
    urllib.request.urlretrieve(URL.format(coords[0], coords[1], zoom, size, size, key), savePath)
    print("Image succesfully retrieved and saved at {}.".format(savePath))

def scrapeCitiesCenterWikipedia(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    divs = soup.findAll("table", {"class": "wikitable sortable"})
    coordinates = [div.text.replace(" ", "").split(';') for div in divs[0].findAll('span', attrs={'class': 'geo'})]
    # print(coordinates)
    with open(COORDINATES_PATH, 'w+') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(coordinates)

def citiesFromCoords(waitTime, startFrom=0):
    with open(COORDINATES_PATH, 'r') as myfile:
        coords_csv = csv.reader(myfile, delimiter=',')
        coords = list(coords_csv)

    for index, coordPair in enumerate(coords[startFrom:]):
        loadSaveImage(coords[index + startFrom], index + startFrom, 12)
        print("wating {} seconds...".format(waitTime))
        time.sleep(waitTime)


if __name__ == "__main__":
    # scrapeCitiesCenterWikipedia('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
    citiesFromCoords(3, 69)
