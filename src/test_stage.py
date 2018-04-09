# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test_stage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

import imageProcess
import inputBox


class Ui_MainWindow(object):
    def __init__(self):
        self.absPath = './../res/'
        self.deviceName = 'device'
        self.sideName = 'side'
        self.sideNum = 1
        self.sideBox = inputBox.App("Enter the Side number")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.button_start_test.setSizePolicy(sizePolicy)
        self.button_start_test.setObjectName("button_start_test")
        self.verticalLayout.addWidget(self.button_start_test)
        self.button_show_result = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_show_result.sizePolicy().hasHeightForWidth())
        self.button_show_result.setSizePolicy(sizePolicy)
        self.button_show_result.setObjectName("button_show_result")
        self.verticalLayout.addWidget(self.button_show_result)
        self.button_capture = QtWidgets.QPushButton(self.frame)
        self.button_capture.setGeometry(QtCore.QRect(10, 80, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.button_capture.setFont(font)
        self.button_capture.setObjectName("button_capture")
        # connect the image capture method
        self.button_capture.clicked.connect(self.img_capture)


        self.button_capture_next = QtWidgets.QPushButton(self.frame)
        self.button_capture_next.setGeometry(QtCore.QRect(170, 150, 161, 21))
        self.button_capture_next.setObjectName("button_capture_next")
        self.button_device_number = QtWidgets.QPushButton(self.frame)
        self.button_device_number.setGeometry(QtCore.QRect(10, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.button_device_number.setFont(font)
        self.button_device_number.setObjectName("button_device_number")
        self.button_device_number.clicked.connect(self.setDeviceNum)

        self.graphicsView = QtWidgets.QLabel(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(370, 60, 401, 391))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setText("Cannot load the image Please Capture button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Test Stage"))
        self.button_start_test.setText(_translate("MainWindow", "Start Test"))
        self.button_show_result.setText(_translate("MainWindow", "Show Result"))
        self.button_capture.setText(_translate("MainWindow", "Capture"))
        self.button_capture_next.setText(_translate("MainWindow", "Next"))
        self.button_device_number.setText(_translate("MainWindow", "Device #"))

    def setDeviceNum(self):
        self.sideBox.do_UI()
        sidedir = self.sideName + self.sideBox.getValue()
        path = self.absPath + self.deviceName + '/' + sidedir
        print('##-PATH : ' + path)

    def img_capture(self):
        print('##-CAPTURE BUTTON PRESSED')
        img = imageProcess.test_image_capture()
        img_ = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
        self.graphicsView.setPixmap(QPixmap.fromImage(img_))

    def do_Nextbutton(self):
        print()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())