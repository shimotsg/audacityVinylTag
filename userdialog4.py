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
import query4


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # set window title and add widgets
        self.setWindowTitle("VinylTag")
        # user input boxes to get artist and album strings
        self.artistIn = QtWidgets.QLineEdit()
        # self.albumIn = QtWidgets.QLineEdit()
        # button for executing query
        self.searchButton = QtWidgets.QPushButton("search")
        # set the appearance and order of buttons and boxes
        # self.text = QtWidgets.QTextBrowser()
        self.layout = QtWidgets.QFormLayout()
        # instantiate and insert the separate widgets into the layout
        self.layout.addWidget(QtWidgets.QLabel("artist"))
        self.layout.addWidget(self.artistIn)

        self.layout.addWidget(self.searchButton)

        # # artist results text
        # self.artistList = QtWidgets.QListWidget()
        # self.layout.addWidget(self.artistList)
        #
        # # results text
        # # album results widget
        self.albumList = QtWidgets.QListWidget()
        self.layout.addWidget(self.albumList)

        # results text
        self.trackList = QtWidgets.QListWidget()
        self.layout.addWidget(self.trackList)

        self.setLayout(self.layout)
        # ties button to function
        self.searchButton.clicked.connect(self.call_mb_query)
        # ties clicking result to getting tracklist
        self.albumList.itemClicked.connect(self.clicked_release)

        self.master_query = query4.mbQuery(self.artistIn.text())

    @Slot()
    def call_mb_query(self):
        self.albumList.clear()

        self.master_query = query4.mbQuery(self.artistIn.text())

        self.master_query.with_input_browse_recordings()
        self.master_query.MB_releaseID = self.master_query.MB_queryResult['release-list'][0]['id']
        for item in self.master_query.MB_queryResult['release-list']:
            self.albumList.addItem(item['title'])

    @Slot()
    def clicked_release(self):
        self.trackList.clear()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
