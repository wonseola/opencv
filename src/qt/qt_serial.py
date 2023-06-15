from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import serial

class mainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.inputLineEdit = QLineEdit(self)
        self.sendButton = QPushButton('aaaa', self)
        self.sendButton.clicked.connect(self.sendText)

        inputlay = QHBoxLayout()
        inputlay.addWidget(self.inputLineEdit)
        inputlay.addWidget(self.sendButton)
        layout = QVBoxLayout(self)
        layout.addLayout(inputlay)

        self.resize(500, 500)

    def sendText(self):
        input = self.inputLineEdit.text()
        # 시리얼통신으로 문자열 전송.....
        # print(input)
        ser.write(input.encode())
        self.inputLineEdit.setText('') # 전송하고 초기화~~~

PORT = "/dev/ttyUSB0"
def prepare():
    global ser
    # 시ㅣ리얼 포트 연결
    ser = serial.serial_for_url(PORT, baudrate = 9600, timeout = 1)




if __name__ == "__main__":
    prepare()
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec_()