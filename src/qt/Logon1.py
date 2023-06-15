from PySide2.QtWidgets import *
import sys
import PySide2.QtCore

class MyForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle('d')
        self.resize(200,300)

        # button
        self.button = QPushButton('&ok', self)
        self.button.clicked.connect(self.okButtonClicked)

        # checkbox
        self.checkBox = QCheckBox('&aaaaaaaaa', self)
        self.checkBox.toggled.connect(self.onCheck)

        # radio button
        box = QGroupBox('00', self)
        self.radio1 = QRadioButton('&01', box)
        self.radio2 = QRadioButton('&02', box)
        self.radio1.setChecked(True)

        groupBoxLayout = QVBoxLayout(box)
        groupBoxLayout.addWidget(self.radio1)
        groupBoxLayout.addWidget(self.radio2)
        self.radio1.toggled.connect(self.choose)

        # layout
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.button)
        mainlayout.addWidget(self.checkBox)
        mainlayout.addWidget(box)

        self.setLayout(mainlayout)


    def okButtonClicked(self):
        print('clicked')

    def onCheck(self, toggle):
        print('checkbox', toggle)
    
    def choose(self, toggle):
        print('radio1', toggle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()

    app.exec_()
