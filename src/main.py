# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
import test_stage
import training_stage
import inputBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Interface(object):
    def __init__(self):
        #set up the next stage
        self.test_Window = QtWidgets.QMainWindow()
        self.test_interface =  test_stage.Ui_MainWindow()
        self.test_interface.setupUi(self.test_Window)

        self.training_Window = QtWidgets.QMainWindow()
        self.training_interface = training_stage.Ui_MainWindow()
        self.training_interface.setupUi(self.training_Window)

        self.inputbox = inputBox.App("Enter the device name")
    def setupUi(self, Interface):
        self.Interace = Interface
        Interface.setObjectName("Interface")
        Interface.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Interface)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 741, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.button_training_stage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_training_stage.setEnabled(True)
        self.button_training_stage.setMinimumSize(QtCore.QSize(1, 50))
        self.button_training_stage.setObjectName("button_training_stage")
        #button push
        self.button_training_stage.clicked.connect(self.go_training_stage)

        self.verticalLayout.addWidget(self.button_training_stage)

        self.button_test_stage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_test_stage.setMinimumSize(QtCore.QSize(1, 50))
        self.button_test_stage.setObjectName("button_test_stage")
        self.button_test_stage.clicked.connect(self.go_test_stage)
        self.verticalLayout.addWidget(self.button_test_stage)

        self.button_statistic_stage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_statistic_stage.setMinimumSize(QtCore.QSize(1, 50))
        self.button_statistic_stage.setObjectName("button_statistic_stage")
        # self.button_statistic_stage.clicked.connect(self.create_inputBox)
        self.verticalLayout.addWidget(self.button_statistic_stage)
        Interface.setCentralWidget(self.centralwidget)

        self.retranslateUi(Interface)

        QtCore.QMetaObject.connectSlotsByName(Interface)

    def retranslateUi(self, Interface):
        _translate = QtCore.QCoreApplication.translate
        Interface.setWindowTitle(_translate("Interface", "MainWindow"))
        self.button_training_stage.setText(_translate("Interface", "Training Stage"))
        self.button_test_stage.setText(_translate("Interface", "Test Stage"))
        self.button_statistic_stage.setText(_translate("Interface", "Statistic & Result"))

    def go_test_stage(self):
        self.inputbox.do_UI()
        print("##RETURN  VALUE : " + self.inputbox.getValue())
        self.test_interface.deviceName = self.inputbox.getValue()
        self.test_Window.show()
        self.Interace.hide()
        print("##-STAGE CHANGED(Test Stage)")

    def go_training_stage(self):
        self.inputbox.do_UI()
        print("##-RETURN  VALUE : " + self.inputbox.getValue())
        self.training_interface.dirName = self.inputbox.getValue()
        self.training_Window.show()
        self.Interace.hide()
        print("##-STAGE CHANGED(Training Stage)")

    def create_inputBox(self):
        print("return value : " + self.inputbox.getValue())
        #print(self.inputbox.text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    Interface = QtWidgets.QMainWindow()
    ui = Ui_Interface()
    ui.setupUi(Interface)
    Interface.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



