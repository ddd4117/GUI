import cv2
import numpy as np


from PyQt5.QtGui import QImage
from ipywidgets import Image


def image_capture(dirPath):
    cap = cv2.VideoCapture(0)
    # Read image
    ret, img = cap.read()
    fromCenter = False


    i = 1
    while True:
        r = cv2.selectROI("Select ROI", img, fromCenter)
        while True:
            imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                filename = "/test" + str(i) +".jpg"
                i += 1
                cv2.imwrite(dirPath + filename, imCrop)
                print("##-COMPLETE SAVE FILE : " + filename)
                break
            elif cv2.waitKey(1) & 0xFF == ord('s'):
                print("##-IMAGE PROCESS COMPELTE")
                cv2.destroyAllWindows()
                return

if __name__ == '__main__':
    image_capture()


