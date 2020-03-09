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
        # self.text = QtWidgets.QTextBrowser()

        self.layout = QtWidgets.QFormLayout()
        # instantiate and insert the separate widgets into the layout
        self.layout.addWidget(QtWidgets.QLabel("artist"))
        self.layout.addWidget(self.artistIn)

        self.layout.addWidget(QtWidgets.QLabel("album"))
        self.layout.addWidget(self.albumIn)
        self.layout.addWidget(self.searchButton)

        # results text
        self.albumList = QtWidgets.QListWidget()
        self.layout.addWidget(self.albumList)

        # self.layout.addWidget(self.text)

        self.setLayout(self.layout)
        # ties button to function
        # self.searchButton.clicked.connect(self.call_mb_query())
        self.searchButton.clicked.connect(self.call_mb_query)

        # self.groupBox = QtWidgets.QGroupBox("groupBox")
        # self.artistOutText = QtWidgets.QTextBrowser(self.groupBox)

        self.master_query = query3.MB_Query(self.artistIn.text(), self.albumIn.text())

    @Slot()
    def call_mb_query(self):
        tmp_artistIn = self.artistIn.text()
        tmp_albumIn = self.albumIn.text()

        wat = query3.MB_Query(tmp_artistIn, tmp_albumIn)
        # wat.album = queryAlbum
        # wat.artist = queryArtist

        wat.show_choices()
        for item in wat.MB_albumResult['recording-list']:
            # line = release['name'][0] + release['date'][0]
            # self.text.setText(line)
            # print(item['title'])
            self.albumList.addItem(item['title'])

    @Slot()
    def clicked_album(self):
        album = self.albumList.itemClicked()
        self.master_query.MB_releaseID = album['id'][0]

        print(self.master_query)
        # where 'title' = album in self.albumList:
        # self.albums = []
        # self.myQuery = query2.mbQuery
    # # execute query


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
