import PySide2.QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys

import PySide2.QtWidgets

class Mainwindow(QWidget):
    def __init__(self, parent= None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('image viewer')
        self.imageLabel = QLabel()
        self.imageLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setPixmap(QPixmap())

        openBtn = QPushButton('load image')

        layout = QVBoxLayout()
        layout.addWidget(self.imageLabel)
        layout.addWidget(openBtn)

        self.setLayout(layout)

        openBtn.clicked.connect(self.open)
        self.resize(QApplication.primaryScreen().availableSize() * 2 / 5)

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '.' , 'Images (*.png *.jpg)')
        # print(fileName) # 경로
        self.load(fileName)
    
    def load(self, fileName):
        image = QImage(fileName)
        if image.isNull():
            QMessageBox.information(self, QApplication.applicationName(), ('No Image' + fileName))
            self.setWindowTitle('image')
            self.imageLabel.setPixmap(QPixmap())
            return
        self.imageLabel.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Mainwindow()
    mainWindow.show()

    app.exec_()

