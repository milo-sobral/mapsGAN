from PIL import Image
import os


IMAGE_PATH = os.path.abspath('../data/raw_roadmap/')
DATASET_PATH = os.path.abspath('../data/dataset_roadmap/big')
DATASET_PATH_SMALL = os.path.abspath('../data/dataset_roadmap/small')
REMOVE_TEXT_PAD = 20
DIVISION_NUMS = 4
ROTATIONS = [Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270]


def removeText(image):
    width, height = image.size
    cropped = image.crop((0, 0, width - REMOVE_TEXT_PAD, height - REMOVE_TEXT_PAD))
    return cropped

def divideImage(image):
    width, height = image.size
    images = []
    count = 0
    for i in range(0, DIVISION_NUMS):
        for j in range(0, DIVISION_NUMS):
            cropped = image.crop((i * (width / DIVISION_NUMS), j * (height / DIVISION_NUMS), (i+1) * (width / DIVISION_NUMS), (j+1) * (height / DIVISION_NUMS)))
            images.append(cropped)
    return images

def rotateImage(image):
    images = [image.transpose(rot) for rot in ROTATIONS]
    return images


def ApplyToAll(path, function, overwrite=True):
    allImages = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for image in allImages:
        print("opening image {}".format(image))
        name = os.path.basename(image)
        im = Image.open(os.path.join(path, image))
        print("applying funtion to image...")
        res = function(im)
        if isinstance(res, list):
            for index, im in enumerate(res):
                name = '{}{}'.format(name, index).replace(".png", "")
                im.save(os.path.join(DATASET_PATH_SMALL, name + ".png"))
        else:
            if overwrite:
                res.save(os.path.join(DATASET_PATH, "{}.png".format(name)))
            else:
                res.save(os.path.join(DATASET_PATH, "{}2.png".format(name)))


if __name__ == '__main__':
    ApplyToAll(DATASET_PATH_SMALL, rotateImage)
    # image = Image.open(os.path.join(DATASET_PATH, "0_12_satellite.png"))
    # res = divideImage(image)
    # for index, im in enumerate(res):
    #     im.save(os.path.join(DATASET_PATH, '{}{}.png'.format("0_12_satellite.png".replace(".png", ""), index)))
