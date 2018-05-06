# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test_stage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import cv2
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtCore import Qt

import imageProcess
import inputBox


class Ui_MainWindow(object):
    def __init__(self, _mainUI = None):
        self.absPath = './../res/'
        self.deviceName = 'device'
        self.sideName = 'side'
        self.sideNum = 1
        self.sideBox = inputBox.App("Enter the Side name")
        self.deviceBox = inputBox.App("Enter the Device Name")
        self.img = numpy.ndarray
        self.imgview = QImage
        self.mainUI = _mainUI

    def setupUi(self, _mainwindow):
        css = """QPushButton { background-color: white;
                        border-style: outset;
                        border-width: 2px;
                        border-radius: 15px;    
                        border-color: black;
                        padding: 4px;
                    }"""
        font = QFont('D2Coding', 25, QFont.Light)
        font2 = QFont('D2Coding', 12, QFont.Light)
        self.MainWindow = _mainwindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 600)
        pal = self.MainWindow.palette()
        pal.setColor(self.MainWindow.backgroundRole(), Qt.white)
        self.MainWindow.setPalette(pal)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font3 = QFont('D2Coding', 25, QFont.Light)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 781, 41))

        self.label.setFont(font3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Home Button
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(730, 10, 50, 50))
        self.home.clicked.connect(self.do_Home)
        self.home.setStyleSheet(css)
        self.home.setFont(font2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 781, 491))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 341, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 321, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_start_test = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.button_start_test.sizePolicy().hasHeightForWidth())

        #Start Button
        self.button_start_test.setSizePolicy(sizePolicy)
        self.button_start_test.setFont(font)
        self.button_start_test.setObjectName("button_start_test")
        self.button_start_test.clicked.connect(self.do_startTest)
        self.button_start_test.setStyleSheet(css)
        self.button_start_test.setFont(font)
        self.verticalLayout.addWidget(self.button_start_test)

        self.button_show_result = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_show_result.sizePolicy().hasHeightForWidth())
        #Show Button
        self.button_show_result.setSizePolicy(sizePolicy)
        self.button_show_result.setObjectName("button_show_result")
        self.button_show_result.setFont(font)
        self.button_show_result.setStyleSheet(css)
        self.button_show_result.clicked.connect(self.show_Result)
        self.verticalLayout.addWidget(self.button_show_result)

        #Capture button
        self.button_capture = QtWidgets.QPushButton(self.frame)
        self.button_capture.setGeometry(QtCore.QRect(10, 80, 321, 61))
        self.button_capture.setFont(font)
        self.button_capture.setObjectName("button_capture")
        self.button_capture.setStyleSheet(css)
        # connect the image capture method
        self.button_capture.clicked.connect(self.img_capture)

        #Next Button
        self.button_capture_next = QtWidgets.QPushButton(self.frame)
        self.button_capture_next.setGeometry(QtCore.QRect(170, 150, 161, 30))
        self.button_capture_next.setObjectName("button_capture_next")
        self.button_capture_next.clicked.connect(self.do_Nextbutton)
        self.button_capture_next.setFont(font2)
        self.button_capture_next.setStyleSheet(css)

        #Set Device Number
        self.button_device_number = QtWidgets.QPushButton(self.frame)
        self.button_device_number.setGeometry(QtCore.QRect(10, 10, 321, 61))
        self.button_device_number.setObjectName("button_device_number")
        self.button_device_number.clicked.connect(self.setDeviceNum)
        self.button_device_number.setStyleSheet(css)
        self.button_device_number.setFont(font)

        self.graphicsView = QtWidgets.QLabel(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(370, 60, 401, 391))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setText("Cannot load the image Please Capture button")
        self.graphicsView.setAlignment(QtCore.Qt.AlignCenter)

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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Test Stage"))
        self.button_start_test.setText(_translate("MainWindow", "Start Test"))
        self.button_show_result.setText(_translate("MainWindow", "Show Result"))
        self.button_capture.setText(_translate("MainWindow", "Capture"))
        self.button_capture_next.setText(_translate("MainWindow", "Next"))
        self.button_device_number.setText(_translate("MainWindow", "Device #"))
        self.home.setText(_translate("MainWindow", "Home"))

    def do_Home(self):
        print("##-Return Home Stage")
        self.mainUI.show()
        self.MainWindow.close()

    def setDeviceNum(self):

        self.deviceBox.do_UI()
        self.deviceName = self.deviceBox.getValue()
        self.sideBox.do_UI()
        self.sideName = self.sideBox.getValue()
        path = self.absPath + self.deviceName + '/' + self.sideName
        print('##-PATH : ' + path)

    def img_capture(self):
        print('##-CAPTURE BUTTON PRESSED')
        self.img = imageProcess.test_image_capture()
        self.imgview = QImage(self.img.data, self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.graphicsView.setPixmap(QPixmap.fromImage(self.imgview))

    def do_Nextbutton(self):
        print("##-NEXT BUTTON CLICKED")

    def do_startTest(self):
        print("##-TEST BUTTON CLICKED")
        ## You write the To-do method here

    def show_Result(self):
        print("##-SHOW RESULT BUTTON CLICKED")
        ## You write the To-do method here and Set result
        self.graphicsView.setText("RESULT DATA")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())