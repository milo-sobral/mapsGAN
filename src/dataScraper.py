import urllib.request
import os

IMAGE_PATH = os.path.abspath('../data/images/')
URL = 'https://maps.googleapis.com/maps/api/staticmap?center={}, {}&zoom={}&size={}x{}&maptype=satellite&key=AIzaSyBu4q6kdUBDAClY2io6kYBQAgjPdvN6AKQ'

def loadSaveImage(coords):
    saveName = "{}_"
    urllib.request.urlretrieve(, saveName)
