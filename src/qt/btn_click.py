import PySide2.QtGui
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys

class MainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.rightPress = False
        self.mousePosLocalLabel = QLabel('', self)
        self.mousePosScreenLabel = QLabel('', self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.mousePosLocalLabel)
        layout.addWidget(self.mousePosScreenLabel)
        self.setLayout(layout)
        self.resize(500, 500)

    def mousePressEvent(self, event:QMouseEvent):
        self.mousePosLocalLabel.setText(f'({event.localPos().x()}, {event.localPos().y()})')
        self.mousePosScreenLabel.setText(f'({event.screenPos().x()}, {event.screenPos().y()})')
        self.mousePosLocalLabel.setText(f'({event.x()}, {event.y()})')
        self.mousePosScreenLabel.setText(f'({event.globalX()}, {event.globalY()})')

        if event.button() == Qt.RightButton:
            self.rightPress = True
        return
    
    def mouseReleaseEvent(self, event:QMouseEvent):
        if event.button() == Qt.RightButton:
            self.rightPress = False
        return
    
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        
        return
    
    def mouseMoveEvent(self, event:QMouseEvent):

        if self.rightPress:
            self.mousePosLocalLabel.setText(f'({event.x()}, {event.y()})')
            self.mousePosScreenLabel.setText(f'({event.globalX()}, {event.globalY()})')

        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()