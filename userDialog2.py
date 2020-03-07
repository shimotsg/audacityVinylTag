# 2/27/2020
# geoffrey shimotsu
# create dialog windows for user input to filter MBID query
# and display album choices
# using example code from qt website
import sys
import random
# import query
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Slot


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # set window title and add widgets
        self.setWindowTitle("VinylTag")
        # user input boxes to get artist and album strings
        self.artistIn = QtWidgets.QLineEdit()
        self.albumIn = QtWidgets.QLineEdit()
        # button for executing query
        self.searchButton = QtWidgets.QPushButton("search")
        # set the appearance and order of buttons and boxes
        self.layout = QtWidgets.QFormLayout()
        # instantiate and insert the separate widgets into the layout
        self.layout.addWidget(QtWidgets.QLabel("artist"))
        self.layout.addWidget(self.artistIn)
        self.layout.addWidget(QtWidgets.QLabel("album"))
        self.layout.addWidget(self.albumIn)
        self.layout.addWidget(self.searchButton)
        self.setLayout(self.layout)
        # ties button to function
        self.searchButton.clicked.connect(self.mbQuery)
        # self.albums = []

    # execute query
    # @Slot()
    def mbQuery(self):
        queryArtist = self.artistIn.text()
        queryAlbum = self.albumIn.text()

        albums = []

        albums.append(queryArtist)
        albums.append(queryAlbum)

        # self.text.setText(random.choice(self.hello))
        print(albums)
        print(self.artistIn.text())
        print(self.albumIn.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
