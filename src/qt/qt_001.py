from PySide2.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(300,150)
    window.setWindowTitle('ddd')
    label = QLabel('hello qt',window)
    label.move(110,75)

    window.show()
    app.exec_()