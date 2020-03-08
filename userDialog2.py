# 2/27/2020
# geoffrey shimotsu
# create dialog windows for user input to filter MBID query
# and display album choices
# using example code from qt website
import sys
import random
# import query
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Slot, Qt
import query3


class MainWindow(QtWidgets.QWidget):

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
        self.text = QtWidgets.QTextBrowser()

        self.layout = QtWidgets.QFormLayout()
        # instantiate and insert the separate widgets into the layout
        self.layout.addWidget(QtWidgets.QLabel("artist"))
        self.layout.addWidget(self.artistIn)

        self.layout.addWidget(QtWidgets.QLabel("album"))
        self.layout.addWidget(self.albumIn)
        self.layout.addWidget(self.searchButton)

        # results text

        self.layout.addWidget(self.text)

        self.setLayout(self.layout)
        # ties button to function
        # self.searchButton.clicked.connect(self.call_mb_query())
        self.searchButton.clicked.connect(self.call_mb_query)

        # self.groupBox = QtWidgets.QGroupBox("groupBox")
        # self.artistOutText = QtWidgets.QTextBrowser(self.groupBox)



        # self.albums = []
        # self.myQuery = query2.mbQuery
    # execute query

    @Slot()
    def call_mb_query(self):
        tmp_artistIn = self.artistIn.text()
        tmp_albumIn = self.albumIn.text()

        wat = query3.MB_Query(tmp_artistIn, tmp_albumIn)
        # wat.album = queryAlbum
        # wat.artist = queryArtist

        wat.show_choices()
        for release in wat.MB_albumResult:
            line = release['name'][0] + release['date'][0]
            self.text.setText(line)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
