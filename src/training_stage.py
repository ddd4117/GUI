# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\training_stage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
import train.train as train

import imageProcess
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 781, 491))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 341, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 140, 321, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.button_start_roi = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start_roi.sizePolicy().hasHeightForWidth())
        self.button_start_roi.setSizePolicy(sizePolicy)
        self.button_start_roi.setObjectName("button_start_roi")
        self.gridLayout.addWidget(self.button_start_roi, 0, 0, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy)
        self.button_delete.setObjectName("button_delete")
        self.gridLayout.addWidget(self.button_delete, 0, 1, 1, 1)
        self.button_show_roi = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_show_roi.sizePolicy().hasHeightForWidth())
        self.button_show_roi.setSizePolicy(sizePolicy)
        self.button_show_roi.setObjectName("button_show_roi")
        self.gridLayout.addWidget(self.button_show_roi, 1, 0, 1, 1)
        self.button_all_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_all_delete.sizePolicy().hasHeightForWidth())
        self.button_all_delete.setSizePolicy(sizePolicy)
        self.button_all_delete.setObjectName("button_all_delete")
        self.gridLayout.addWidget(self.button_all_delete, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 321, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_training = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_training.sizePolicy().hasHeightForWidth())
        self.pushButton_training.setSizePolicy(sizePolicy)
        self.pushButton_training.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_training)
        #this button calls make_mode method
        self.pushButton_training.clicked.connect(self.make_model)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.button_capture = QtWidgets.QPushButton(self.frame)
        self.button_capture.setGeometry(QtCore.QRect(10, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.button_capture.setFont(font)
        self.button_capture.setObjectName("button_capture")
        self.button_capture.clicked.connect(self.do_Capture)
        #connect method

        self.button_capture_next = QtWidgets.QPushButton(self.frame)
        self.button_capture_next.setGeometry(QtCore.QRect(170, 80, 161, 21))
        self.button_capture_next.setObjectName("button_capture_next")
        # self.button_capture_next.clicked.connect(self.getInteger)

        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(370, 60, 401, 391))
        self.graphicsView.setObjectName("graphicsView")
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
        self.label.setText(_translate("MainWindow", "Training Stage"))
        self.button_start_roi.setText(_translate("MainWindow", "Start ROI"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_show_roi.setText(_translate("MainWindow", "Show ROI"))
        self.button_all_delete.setText(_translate("MainWindow", "All Delete"))
        self.pushButton_training.setText(_translate("MainWindow", "Training Start"))
        self.pushButton.setText(_translate("MainWindow", "Create Training Image"))
        self.button_capture.setText(_translate("MainWindow", "Capture"))
        self.button_capture_next.setText(_translate("MainWindow", "Next"))
    def do_Capture(self):
        print("image Capture - Start")
        imageProcess.image_capture()


    def getInteger(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

    def make_model(self):
        path = 'test/testdevice1'
        print("Training device: " + path)
        train.training(path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

