# 2/27/2020
# geoffrey shimotsu
# create dialog windows for user input to filter MBID query
# and display album choices
# using example code from qt website
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import query3


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # set window title and add widgets
        self.setWindowTitle("VinylTag")
        # user input boxes to get artist and album strings
        self.artistIn = QLineEdit()
        self.albumIn = QLineEdit()
        # button for executing query
        self.searchButton = QPushButton("search")
        # set the appearance and order of buttons and boxes
        self.text = QTextBrowser()

        self.layout = QFormLayout()
        # instantiate and insert the separate widgets into the layout
        self.layout.addWidget(QLabel("artist"))
        self.layout.addWidget(self.artistIn)

        self.layout.addWidget(QLabel("album"))
        self.layout.addWidget(self.albumIn)
        self.layout.addWidget(self.searchButton)

        # results text

        self.layout.addWidget(self.text)

        self.setLayout(self.layout)
        # ties button to function
        self.searchButton.clicked.connect(self.call_mb_query())

        self.groupBox = QGroupBox("groupBox")
        self.artistOutText = QTextBrowser(self.groupBox)

        # self.albums = []
        # self.myQuery = query2.mbQuery

    # execute query

    @Slot()
    def call_mb_query(self):
        queryArtist = self.artistIn.text()
        queryAlbum = self.albumIn.text()

        print(queryAlbum)
        print(queryAlbum)

        wat = query3.MB_Query(queryArtist, queryAlbum)
        # wat.album = queryAlbum
        # wat.artist = queryArtist
        # self.artistOutText.setText(wat.show_choices())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
