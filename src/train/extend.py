import cv2, os, PIL
from PIL import Image

def convert(image):
    width, height = image.size
    if width > height :
        new = image.resize((300, round( 300 * (height / width) )))
    else :
        new = image.resize( ( round( 300 * (width / height) ) , 300))

    return new

def correct(image):
    width, height = image.size
    new = convert( image.crop( ( 20, 20, width - 20, height - 20 ) ) )
    return new

def save(image, path, index):
    filename = path.split('.')[0]
    image.save(filename + str(index) +'1.jpg')
    new = correct( image.rotate(3) )
    new.save(filename + str(index) + '2.jpg')
    new = correct( image.rotate(-3) )
    new.save(filename + str(index) + '3.jpg')
    new = correct( image.rotate(5) )
    new.save(filename + str(index) + '4.jpg')
    new = correct( image.rotate(-5) )
    new.save(filename + str(index) + '5.jpg')

def extend(path):
    print('extending: ', path)
    files = os.listdir(path)
    for image in files:
        image_path = path + '/' + image
        origin = Image.open(image_path)
        image = convert(origin)
        width, height = image.size
        area = (0, 0, width - 20, height - 20)
        new = convert( image.crop( area ) )
        save(new, image_path, 1)

        area = (20, 0, width, height - 20)
        new = convert(image.crop(area))
        save(new, image_path, 2)

        area = (0, 20, width - 20, height)
        new = convert(image.crop(area))
        save(new, image_path, 3)

        area = (20, 20, width, height)
        new = convert(image.crop(area))
        save(new, image_path, 4)