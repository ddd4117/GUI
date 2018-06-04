import os, PIL
from PIL import Image

def convert(image):
    width, height = image.size
    if width > height :
        new = image.resize((500, round( 500 * (height / width) )))
    else :
        new = image.resize( ( round( 500 * (width / height) ) , 500))

    return new

def correct(image):
    width, height = image.size
    new = convert( image.crop( ( 20, 20, width - 20, height - 20 ) ) )
    return new

def save(image, path, index):
    filename = path
    image.save(filename + str(index) +'1.jpg')
    new = correct( image.rotate(3) )
    new.save(filename + str(index) + '2.jpg')
    new = correct( image.rotate(-3) )
    new.save(filename + str(index) + '3.jpg')
    new = correct( image.rotate(5) )
    new.save(filename + str(index) + '4.jpg')
    new = correct( image.rotate(-5) )
    new.save(filename + str(index) + '5.jpg')

def extend(new_path, origin_path):
    print('extending: {0} from {1}.'.format(new_path, origin_path))
    files = os.listdir(origin_path)
    for file in files:
        image_path = new_path + '/' + file.split('.')[0] + '_'
        origin = Image.open(origin_path + '/' + file)
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