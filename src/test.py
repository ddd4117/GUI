import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

qtCreatorFile = "test_stage.ui"
test_stage_file = "test_stage.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    xwin = MyApp()

    app.exec()

