# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\training_stage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QState
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
import train
import imageProcess
from PyQt5.QtCore import Qt
import pathlib
import config

class Ui_MainWindow(object):
    def __init__(self, _mainUI = None):
        self.absPath = './../res/'
        self.dirName = 'device'
        self.side = 'side'
        self.sideNum = 1
        self.cameraNum = 0
        self.mainUI = _mainUI
    def setupUi(self, _MainWindow):
        css = """QPushButton { background-color: white;
                                border-style: outset;
                                border-width: 2px;
                                border-radius: 15px;    
                                border-color: black;
                                padding: 4px;
                            }"""
        font = QFont('D2Coding', 18, QFont.Light)
        font2 = QFont('D2Coding', 12, QFont.Light)
        self.MainWindow =_MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 600)
        pal = self.MainWindow.palette()
        pal.setColor(self.MainWindow.backgroundRole(), Qt.white)
        self.MainWindow.setPalette(pal)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Title Label
        font3= QFont('D2Coding', 25, QFont.Light)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 781, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setFont(font3)

        self.currentState = QtWidgets.QLabel(self.centralwidget)
        self.currentState.setGeometry(QtCore.QRect(10,71,781,21))
        self.currentState.setFont(font2)
        self.currentState.setAlignment(QtCore.Qt.AlignCenter)
        self.currentState.setObjectName('currentState')

        #Home Button
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(730,10,50,50))
        self.home.clicked.connect(self.do_Home)
        self.home.setFont(font2)
        self.home.setStyleSheet(css)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 781, 491))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 341, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 190, 321, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        #ROI Start Button
        # self.button_start_roi = QtWidgets.QPushButton(self.gridLayoutWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.button_start_roi.sizePolicy().hasHeightForWidth())
        # self.button_start_roi.setSizePolicy(sizePolicy)
        # self.button_start_roi.setObjectName("button_start_roi")
        # self.button_start_roi.setFont(font)
        # self.button_start_roi.setStyleSheet(css)
        #
        # self.gridLayout.addWidget(self.button_start_roi, 0, 0, 1, 1)

        # #Delete Button
        # self.button_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        # self.button_delete.setSizePolicy(sizePolicy)
        # self.button_delete.setObjectName("button_delete")
        # self.button_delete.setStyleSheet(css)
        # self.button_delete.setFont(font)

        # self.gridLayout.addWidget(self.button_delete, 0, 1, 1, 1)
        # Show ROI Button
        self.button_show_roi = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_show_roi.sizePolicy().hasHeightForWidth())
        self.button_show_roi.setSizePolicy(sizePolicy)
        self.button_show_roi.setObjectName("button_show_roi")
        self.button_show_roi.setFont(font)
        self.button_show_roi.setStyleSheet(css)
        self.gridLayout.addWidget(self.button_show_roi, 1, 0, 1, 1)
        self.button_show_roi.clicked.connect(self.do_ShowROI)
        #Delete All button
        self.button_all_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_all_delete.sizePolicy().hasHeightForWidth())
        self.button_all_delete.setSizePolicy(sizePolicy)
        self.button_all_delete.setObjectName("button_all_delete")
        self.button_all_delete.setStyleSheet(css)
        self.button_all_delete.setFont(font)
        self.button_all_delete.clicked.connect(self.do_AllDelete)


        self.gridLayout.addWidget(self.button_all_delete, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 321, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #Create Image
        self.button_create_img = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_create_img.sizePolicy().hasHeightForWidth())
        self.button_create_img.setSizePolicy(sizePolicy)
        self.button_create_img.setObjectName("pushButton")
        self.button_create_img.setFont(font)
        self.button_create_img.setStyleSheet(css)
        # this button calls create_image method
        self.button_create_img.clicked.connect(self.create_image)
        self.verticalLayout.addWidget(self.button_create_img)

        # Training Button
        self.pushButton_training = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_training.sizePolicy().hasHeightForWidth())
        self.pushButton_training.setSizePolicy(sizePolicy)
        self.pushButton_training.setObjectName("pushButton_2")
        self.pushButton_training.setStyleSheet(css)
        self.pushButton_training.setFont(font)
        self.verticalLayout.addWidget(self.pushButton_training)
        #this button calls make_mode method
        self.pushButton_training.clicked.connect(self.make_model)

        #Incorrect Capture Button
        self.incorrect_capture = QtWidgets.QPushButton(self.frame)
        self.incorrect_capture.setGeometry(QtCore.QRect(170, 10, 160, 80))
        self.incorrect_capture.setFont(font)
        self.incorrect_capture.setStyleSheet(css)

        #Correct Capture Button
        self.correct_capture = QtWidgets.QPushButton(self.frame)
        self.correct_capture.setGeometry(QtCore.QRect(10, 10, 155, 80))
        self.correct_capture.setFont(font)
        self.correct_capture.setStyleSheet(css)
        self.correct_capture.setFont(font)
        self.correct_capture.setObjectName("correct_capture")
        self.incorrect_capture.setFont(font)
        self.incorrect_capture.setObjectName("Incorrect Capture")
        self.incorrect_capture.clicked.connect(self.do_InCorrect)
        # this button calls do_capture method
        self.correct_capture.clicked.connect(self.do_Capture)

        #Next Button
        self.button_capture_next = QtWidgets.QPushButton(self.frame)
        self.button_capture_next.setGeometry(QtCore.QRect(170, 100, 161, 30))
        self.button_capture_next.setObjectName("button_capture_next")
        self.button_capture_next.setStyleSheet(css)
        self.button_capture_next.setFont(font2)

        self.button_capture_next.clicked.connect(self.do_NextSide)

        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(370, 60, 401, 391))
        self.graphicsView.setObjectName("graphicsView")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    def do_ShowROI(self):
        print("##-SHOW ROI")
        path = self.absPath + self.dirName + '/' + self.side + str(self.sideNum)
        imageProcess.showROI(self.cameraNum, path)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Training Stage"))
        # self.button_start_roi.setText(_translate("MainWindow", "Start ROI"))
        # self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_show_roi.setText(_translate("MainWindow", "Show ROI"))
        self.button_all_delete.setText(_translate("MainWindow", "All Delete"))
        self.pushButton_training.setText(_translate("MainWindow", "Training Start"))
        self.button_create_img.setText(_translate("MainWindow", "Create Training Image"))
        self.correct_capture.setText(_translate("MainWindow", "Correct\nCapture"))
        self.incorrect_capture.setText(_translate("MainWindow", "Incorrect\nCapture"))
        self.button_capture_next.setText(_translate("MainWindow", "Next"))
        self.home.setText(_translate("MainWindow", "Home"))
    def setState(self, _side = 'side1'):
        self.currentState.setText(QtCore.QCoreApplication.translate("MainWindow", self.dirName + " " + _side))
    def do_AllDelete(self):
        deletePath = self.absPath + self.dirName
        config.delete_folder(pathlib.Path(deletePath))
        # if os.path.isdir(deletePath):
        #     print(deletePath)
        #     proc = subprocess.Popen(['rmdir', '/s', '/q', deletePath],
        #                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     out, err = proc.communicate()
        print("##-DELETE ALL")

    def do_Home(self):
        print("##-Return Home Stage")
        self.mainUI.show()
        self.MainWindow.close()

    def do_InCorrect(self):
        # write that you want to do
        print("##-INCORRECT CAPTURE START")
        path = self.absPath + self.dirName
        side = self.side + str(self.sideNum)
        imageProcess.image_capture(path, side, self.cameraNum, False)


    def do_NextSide(self):
        self.cameraNum = (self.cameraNum + 1) % 1 # CAMERA CHANGE
        self.sideNum+=1
        side = self.side + str(self.sideNum)
        self.setState(side)
        print("##-CLIKED THE NEXT BUTTON :" + side)

    def do_Capture(self):
        print("##-IMAGE CAPTURE START")

        path = self.absPath
        config.makeDir(path)

        path += self.dirName
        config.makeDir(path)

        side = self.side + str(self.sideNum)
        config.makeDir(path + '/' + side)

        print("##IMAGE PROCESS PATH IS : " + path)
        imageProcess.image_capture(path, side, self.cameraNum, True)
        print(1)

    def create_image(self):
        #plz write the image path
        path = self.absPath + self.dirName
        print(path)
        train.copy_images(path)
        print('#COPY IMAGES DONE')

    def make_model(self):
        #plz write the device path
        path = self.absPath + self.dirName
        print("Training device: " + path)
        train.execute_Train(self.dirName, path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

