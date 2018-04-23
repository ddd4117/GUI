import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self, subtitle = "Enter", choose = 0):
        super().__init__()
        self.title = 'GUI'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.subtitle = subtitle
        self.val = ''
        self.okPressed = False
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.hide()
        # self.do_UI()


    def do_UI(self):
        self.val, self.okPressed = QInputDialog.getText(self, "Get text", self.subtitle, QLineEdit.Normal, "")

    def getValue(self):
        if self.okPressed and self.val != '':
            return self.val
        else:
            return "NONE"

            # def getInteger(self):
            #     i, okPressed = QInputDialog.getInt(self, "Get integer", "Percentage:", 28, 0, 100, 1)
            #     if okPressed:
            #         print(i)
            #
            # def getDouble(self):
            #     d, okPressed = QInputDialog.getDouble(self, "Get double", "Value:", 10.50, 0, 100, 10)
            #     if okPressed:
            #         print(d)
            #
            # def getChoice(self):
            #     items = ("Red", "Blue", "Green")
            #     item, okPressed = QInputDialog.getItem(self, "Get item", "Color:", items, 0, False)
            #     if okPressed and item:
            #         print(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.do_UI()
    sys.exit(app.exec_())