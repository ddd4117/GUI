# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Interface(object):
    def setupUi(self, Interface):
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
        self.verticalLayout.addWidget(self.button_training_stage)
        self.button_test_stage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_test_stage.setMinimumSize(QtCore.QSize(1, 50))
        self.button_test_stage.setObjectName("button_test_stage")
        self.verticalLayout.addWidget(self.button_test_stage)
        self.button_statistic_stage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_statistic_stage.setMinimumSize(QtCore.QSize(1, 50))
        self.button_statistic_stage.setObjectName("button_statistic_stage")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interface = QtWidgets.QMainWindow()
    ui = Ui_Interface()
    ui.setupUi(Interface)
    Interface.show()
    sys.exit(app.exec_())

