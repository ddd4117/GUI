from PIL import Image

def crop(origin, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    print(origin)
    image_obj = Image.open(origin)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location + 'Origin.jpg')
    new(image_obj, coords, saved_location)
    #cropped_image.show()

    # (small x, small y, bigger x, bigger y)

def isinBound(size, coords):
    if coords[0] < 0 or coords[1] < 0 or coords[2] > size[0] or coords[3] > size[1] :
        return False
    else :
        return True

def new(image, coords, saved_location) :
    for i in range(3,7):
        ext_width = round( (coords[2] - coords[0]) / i)
        ext_height = round( (coords[3] - coords[1]) / i)
        size = image.size

        new_coords = (coords[0]-ext_width, coords[1] - ext_height, coords[2], coords[3])
        if isinBound( size, new_coords):
            new_image = image.crop(new_coords)
            new_image.save(saved_location + '_' + str(i) + 'a.jpg')

        new_coords = (coords[0], coords[1] - ext_height, coords[2] + ext_width, coords[3])
        if isinBound( size, new_coords):
            new_image = image.crop(new_coords)
            new_image.save(saved_location + '_' + str(i) + 'b.jpg')

        new_coords = (coords[0] - ext_width, coords[1], coords[2], coords[3] + ext_height)
        if isinBound(size, new_coords):
            new_image = image.crop(new_coords)
            new_image.save(saved_location + '_' + str(i) + 'c.jpg')

        new_coords = (coords[0], coords[1], coords[2] + ext_width, coords[3] + ext_height)
        if isinBound(size, new_coords):
            new_image = image.crop(new_coords)
            new_image.save(saved_location + '_' + str(i) + 'd.jpg')

        new_coords = (coords[0] - ext_width, coords[1] - ext_height, coords[2] + ext_width, coords[3] + ext_height)
        if isinBound(size, new_coords):
            new_image = image.crop(new_coords)
            new_image.save(saved_location + '_' + str(i) + 'e.jpg')
