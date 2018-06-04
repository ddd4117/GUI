import threading

import cv2
import os
import Crop
import pathlib
import copy
import config
import inputBox
import checkBox
import roiUnit
from PyQt5.QtGui import QImage
from ipywidgets import Image
def writefile(dirPath, img_list):
    myfile = open(dirPath + "/data.txt", 'w+')
    print(dirPath, img_list)
    if(len(img_list) > 0):
        for _img in img_list:
            print(_img[0], _img[1], _img[2], _img[3])
            myfile.write("%s:%s:%s:%s:%s\n" %(_img[0], _img[1], _img[2], _img[3], _img[4]))
            myfile.flush()
    myfile.close()
    print("DONE")

def readfile(dirPath):
    if os.path.isfile(dirPath + "/data.txt"):
        f = open(dirPath + "/data.txt", 'r+')
    else :
        return []

    lines = f.readlines()
    cordiList = []
    for line in lines:
        cordi = line.split(':')
        cordi[0] = int(cordi[0])
        cordi[1] = int(cordi[1])
        cordi[2] = int(cordi[2])
        cordi[3] = int(cordi[3])
        cordi[4] = cordi[4].strip()
        cordiList.append(cordi)
    f.close()
    print(cordiList)
    return cordiList

def getImage(cameraNum, conf) :
    cap = cv2.VideoCapture(cameraNum)
    cap.set(3, int(conf['width']))
    cap.set(4, int(conf['height']))

    if config.AUTO_FOCUS:
        while True:
            ret, img = cap.read()
            cv2.imshow('Video', img)
            if cv2.waitKey(10) & 0xFF == 27:
                break
    else :
        ret, img = cap.read()

    cap.release()
    cv2.destroyAllWindows()
    print('# GET IMAGE FROM CAMERA#{}, AUTO_FOCUS: {}'.format(cameraNum, config.AUTO_FOCUS))
    return img

def convert(coord, conf):
    widthRatio = conf['width_ratio']
    heightRatio = conf['height_ratio']
    newCoord = ( int(coord[0] * widthRatio),
                 int(coord[1] * heightRatio),
                 int((coord[0] + coord[2]) * widthRatio),
                 int((coord[1] + coord[3]) * heightRatio))
    return newCoord

def image_capture(dirPath, side, cameraNum, doWriteROI):
    print(dirPath)
    if doWriteROI : file = open(dirPath + '/' + 'locationInfo.txt', "a+")
    roiList = readfile(dirPath+"/"+side)
    img_path_list = []
    selected_img = roiList
    inputbox = inputBox.App("Enter the Object Name")

    origin = getImage(cameraNum, config.WINDOW_SIZE)
    cv2.imwrite(dirPath + "/Origin.jpg", origin)
    origin_path = dirPath + "/Origin.jpg"

    img = getImage(cameraNum, config.TESTWINDOW_SIZE)
    fromCenter = False
    dirPath = dirPath + '/' + side
    elements = {}
    first_img = copy.copy(img)
    fileName_idx = 1

    while True:
        if (len(selected_img) > 0):
            for rect in (selected_img):
                if (rect[4] == True) or (rect[4] == 'True'):
                    cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
                else:
                    cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 0), 3)
        r = cv2.selectROI("Select ROI", img, fromCenter)
        while True:
            # imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                inputbox.do_UI()
                objName = inputbox.getValue()
                if objName in elements : elements[objName] += 1
                else : elements[objName] = 0
                x = r[0]
                y = r[1]
                w = r[2]
                h = r[3]
                dirName = side + '_' + objName + '_' + str(elements[objName])
                if doWriteROI == True : dirName += '_cor'
                else : dirName += '_incor'
                temppath = dirPath + '/' + dirName

                fileName = temppath + '/' + side + '_' + objName
                config.makeDir(temppath)
                # cv2.imwrite(temppath + '/' + filename, imCrop)
                coord = convert(r, config.WINDOW_RATIO)
                Crop.crop(origin_path, coord, fileName + '_' + str(elements[objName]))
                img_path_list.append(temppath)
                selected_img.append([x, y, w, h, doWriteROI])
                if doWriteROI :
                    file.write("%s_%s_%s_%s_%s_%s_%s\n" % (x, y, w, h, side, objName, elements[objName]))
                    file.flush()
                    print("##-COMPLETE SAVE FILE : " + objName)
                break
            elif cv2.waitKey(1) & 0xFF == ord('d'):
                _size = len(img_path_list)
                if(_size > 0):
                    print("##-IMAGE DELETE")
                    _path = img_path_list.pop()
                    print(_path)
                    config.delete_folder(pathlib.Path(_path))
                    # os.remove()
                    selected_img.pop()
                    img = copy.copy(first_img) #before img
                    fileName_idx -= 1
                else:
                    print("##-IMAGE DELETE - FAILED(No File)")
                break
            elif cv2.waitKey(1) & 0xFF == ord('s'):
                print("##-IMAGE PROCESS COMPELTE")
                cv2.destroyAllWindows()
                writefile(dirPath, selected_img)
                if(doWriteROI):
                    file.close()
                return

def test_image_capture(infos, O_path, C_path, cameraNum):
    print('## Test image capture:', O_path, C_path)
    img = getImage(cameraNum, config.WINDOW_SIZE)
    number = 0

    noise_min = config.NOISE_TEST['min']
    noise_max = config.NOISE_TEST['max']

    for info in infos :
        cropped = img[info.startY:info.endY, info.startX:info.endX]
        image_path = O_path + '/' + info.side + '_' + info.element + '_' + info.number + '_' + str(number) + '.jpg'
        cv2.imwrite(image_path, cropped)
        canny = cv2.Canny(cropped, noise_min, noise_max)
        image_path = C_path + '/' + info.side + '_' + info.element + '_' + info.number + '_' + str(number) + '.jpg'
        cv2.imwrite(image_path, canny)
        number +=1

    return cv2.resize(img, (config.TESTWINDOW_SIZE['width'], config.TESTWINDOW_SIZE['height']))

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
    # img_path_list.append(temppath+'/'+filename)
    # selected_img.append([x1,y1,x2,y2])
    file.write("%s_%s_%s_%s_%s_%s\n" % (x1, y1, x2, y2, side, objName))
    file.flush()
    print("##-COMPLETE SAVE FILE : " + objName)

def showROI(cameraNum, dirPath):
    capture = cv2.VideoCapture(cameraNum)
    capture.set(3, int(config.TESTWINDOW_SIZE['width']))
    capture.set(4, int(config.TESTWINDOW_SIZE['height']))
    print(dirPath)
    selected_img = readfile(dirPath)
    while True:
        ret, frame = capture.read()
        if (len(selected_img) > 0):
            for rect in (selected_img):
                if (rect[4] == True) or (rect[4] == 'True'):
                    cv2.rectangle(frame, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
                else:
                    cv2.rectangle(frame, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 0), 3)
        if not ret:
            return

        cv2.imshow('Show ROI', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break;

    capture.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    image_capture()


# def image_capture__(dirPath,  side, cameranum, doWriteROI):
#     print(dirPath)
#     if doWriteROI:
#         file = open(dirPath + '/' + 'locationInfo.txt', "a+")
#     # checkbox = checkBox.MyWindow(dic, 'device2')
#     inputbox = inputBox.App("Enter the Object Name")
#     cap = cv2.VideoCapture(cameranum)
#     # Read image
#     ret, img = cap.read()
#     fromCenter = False
#     dirPath = dirPath + '/' + side
#     first_img = copy.copy(img)
#     fileName_idx = 1
#
#     while True:
#         if(len(selected_img) > 0):
#             for rect in (selected_img):
#                 cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
#
#         r = cv2.selectROI("Select ROI", img, fromCenter)
#
#         while True:
#             imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
#             x1 = r[0]
#             y1 = r[1]
#             x2 = r[2]
#             y2 = r[3]
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 # checkbox.do_UI()
#                 # objName = checkbox.getValue()
#                 cv2.rectangle(img, (x1, y1), (x1 + x2, y1 + y2), (0, 255, 0), 3)
#                 objName = 'testfileA' + str(fileName_idx) #Write the file Name
#                 fileName_idx += 1
#                 filename = objName + ".jpg"
#                 temppath = dirPath + '/' + objName
#                 if not os.path.isdir(temppath):
#                     print('##-DIRECTORY CREATE : ' + temppath)
#                     os.mkdir(temppath)
#                 cv2.imwrite(temppath + '/' + filename, imCrop)
#                 img_path_list.append(temppath + '/' + filename)
#                 selected_img.append([x1, y1, x2, y2])
#                 file.write("%s_%s_%s_%s_%s_%s\n" % (x1, y1, x2, y2, side, objName))
#                 file.flush()
#                 print("##-COMPLETE SAVE FILE : " + objName)
#                 # t = threading.Thread(target=checkclicked, args=(checkbox, dirPath, imCrop, x1, x2, y1, y2, file, side))
#                 # t.daemon = True
#                 # t.start()
#                 break
#             elif cv2.waitKey(1) & 0xFF == ord('d'):
#                 _size = len(img_path_list)
#                 if(_size > 0):
#                     print("##-IMAGE DELETE")
#                     _path = img_path_list.pop()
#                     print(_path)
#                     config.delete_folder(pathlib.Path(_path))
#                     selected_img.pop()
#                     img = copy.copy(first_img) #before img
#                     fileName_idx -= 1
#                 else:
#                     print("##-IMAGE DELETE - FAILED(No File)")
#                 break
#             elif cv2.waitKey(1) & 0xFF == ord('s'):
#                 print("##-IMAGE PROCESS COMPELTE")
#                 cv2.destroyAllWindows()
#                 file.close()
#                 return