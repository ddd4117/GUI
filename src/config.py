import os

CAMERA_NUMBER = 1
IMAGE_SIZE = 128
ITERATION = 10000
BATCH_SIZE = 32

TESTWINDOW_SIZE = {
    'width' : 1632,
    'height' : 1224,
}

WINDOW_SIZE = {
    'width' : 3264,
    'height' : 2448
}

WINDOW_RATIO = {
    'width_ratio' : WINDOW_SIZE['width'] / TESTWINDOW_SIZE['width'],
    'height_ratio' : WINDOW_SIZE['height'] / TESTWINDOW_SIZE['height']
}

GREEN = (0,255,0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)

def makeDir(path):
    # This part is make dir when it doesnt exist
    if not os.path.isdir(path) :
        print('##-PATH CREATE : ' + path)
        os.mkdir(path)
        return True
    return False

def delete_folder(pth) :
    for sub in pth.iterdir() :
        if sub.is_dir() :
            delete_folder(sub)
        else :
            sub.unlink()
    pth.rmdir()
