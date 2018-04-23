import threading

import cv2
import os
import numpy as np

import time
import inputBox
import checkBox
from PyQt5.QtGui import QImage
from ipywidgets import Image

def readfile():
    f = open("./../data.txt", 'r')
    lines = f.readlines()
    f.close()
    dic = {};
    for line in lines:
        left, right = line.split(':')
        temp = list(right.split(','))
        for i in range(len(temp)):
            temp[i] = temp[i].strip()
        dic[left] = temp
    return dic

def image_capture(dirPath, devicename, side):
    dic = readfile()
    print(dic, devicename)
    file = open(dirPath + '/' + 'locationInfo.txt', "a+")
    checkbox = checkBox.MyWindow(dic, 'device2')
    cap = cv2.VideoCapture(0)
    # Read image
    ret, img = cap.read()
    fromCenter = False
    dirPath = dirPath + '/' + side
    # checkbox.do_UI()
    while True:
        r = cv2.selectROI("Select ROI", img, fromCenter)
        while True:
            imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            x1 = r[0]
            y1 = r[1]
            x2 = r[2]
            y2 = r[3]

            if cv2.waitKey(1) & 0xFF == ord('q'):
                checkbox.do_UI()
                t = threading.Thread(target=checkclicked, args=(checkbox, dirPath, imCrop, x1, x2, y1, y2, file, side))
                t.daemon = True
                t.start()
                break
            elif cv2.waitKey(1) & 0xFF == ord('s'):
                print("##-IMAGE PROCESS COMPELTE")
                cv2.destroyAllWindows()
                file.close()
                return

def test_image_capture():
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    return img

def checkclicked(checkbox, dirPath, imCrop, x1, x2, y1, y2, file, side):
    while True:
        if(checkbox.flag):
            break
    print(checkbox.getValue())
    objName = checkbox.getValue()
    filename = objName + ".jpg"
    temppath = dirPath + '/' + objName
    if not os.path.isdir(temppath):
        print('##-DIRECTORY CREATE : ' + temppath)
        os.mkdir(temppath)
    cv2.imwrite(temppath + '/' + filename, imCrop)
    file.write("%s_%s_%s_%s_%s_%s\n" % (x1, y1, x2, y2, side, objName))
    file.flush()
    print("##-COMPLETE SAVE FILE : " + objName)

if __name__ == '__main__':
    image_capture()


