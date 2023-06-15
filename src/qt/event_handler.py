import typing
import PySide2.QtCore
import PySide2.QtGui
from PySide2.QtWidgets import *
import sys

import PySide2.QtWidgets

class mainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def mousePressEvent(self, event):
        print('press : ',event)
        return
    def mouseReleaseEvent(self, event):
        print('release : ',event)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec_()