from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from pytube import YouTube

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()


    def setUI(self):
        
        self.ustAyarlar()
        self.anaMenu()
        self.show()
    def anaMenu(self):
        widget= QWidget()
        hbox= QHBoxLayout()

        yazı = QLabel("YouTube Linkini Giriniz : ")

        self.link=QLineEdit()

        button = QPushButton("İNDİR")

        button.clicked.connect(self.i̇ndi̇r)
        hbox.addWidget(yazı)
        hbox.addWidget(self.link)
        hbox.addWidget(button)

        widget.setLayout(hbox)

        self.setCentralWidget(widget)


    def indir(self):
           
        url = self.link.text()
        YouTube(url).streams.first().download()

    def ustAyarlar(self):
        self.setWindowTitle("HCT YouTube Downloader")

        self.setGeometry(250,250,600,80)
        self.setMaximumSize(1000,80)
        self.setMinimumSize(600,80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())

