import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
from PyQt5.QtGui import QImage
from ipywidgets import Image


def image_capture():

    # Read image
    img = cv2.imread('./../res/image1.png', 1)
    fromCenter = False

    cv2.HoughLinesP
    i = 1
    while True:
        r = cv2.selectROI("Select ROI", img, fromCenter)
        while True:
            imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                path = "./../res/modify_img/"
                filename = "test" + str(i) +".jpg"
                print("Complete save file : " + filename)
                i += 1
                cv2.imwrite(path + filename, imCrop)
                break
            elif cv2.waitKey(1) & 0xFF == ord('s'):
                print("IMAGE PROCESS COMPELTE")
                cv2.destroyAllWindows()
                return

if __name__ == '__main__':
    image_capture()


