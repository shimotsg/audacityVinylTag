# 2/27/2020
# geoffrey shimotsu
# create dialog windows for user input to filter MBID query
# and display album choices
# using example code from qt website
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
import mbQuery

# TODO no error or exception handling

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # set window title and add widgets
        self.setWindowTitle("VinylTag")
        # user input boxes to get artist and album strings
        self.artistIn = QtWidgets.QLineEdit()
        # button for executing query
        self.searchButton = QtWidgets.QPushButton("search")
        # set the appearance and order of buttons and boxes w form layout
        self.layout = QtWidgets.QFormLayout()
        # instantiate and insert the separate widgets into the layout
        self.layout.addWidget(QtWidgets.QLabel("artist"))
        self.layout.addWidget(self.artistIn)
        self.layout.addWidget(self.searchButton)
        # # results text
        # # album results widget
        self.albumList = QtWidgets.QListWidget()
        self.layout.addWidget(self.albumList)
        # get tracks button
        self.get_tracks_button = QtWidgets.QPushButton("get tracks")
        self.layout.addWidget(self.get_tracks_button)
        # results text
        self.trackList = QtWidgets.QListWidget()
        self.layout.addWidget(self.trackList)
        # put form layout in widget
        self.setLayout(self.layout)
        # ties button to function
        self.searchButton.clicked.connect(self.call_mb_query)
        # ties clicking result to getting tracklist
        self.albumList.itemClicked.connect(self.clicked_release)

        # instantiates a parameteric query object
        self.master_query = mbQuery.mbQuery(self.artistIn.text())

        self.get_tracks_button.clicked.connect(self.call_mb_release_id)

        self.write_label_track_button = QtWidgets.QPushButton("write label track txt")
        self.layout.addWidget(self.write_label_track_button)
        self.write_label_track_button.clicked.connect(self.write_label_track)

    # window functions
    # TODO this is dumb and needs to be fixed; different control or data struct
    @Slot()
    def call_mb_query(self):
        self.albumList.clear()

        self.master_query = mbQuery.mbQuery(self.artistIn.text())

        self.master_query.with_input_browse_recordings()

        for item in self.master_query.MB_queryResult['release-list']:
            QtWidgets.QListWidgetItem(item['title'], self.albumList)

    # this sets the album for tracklist
    @Slot()
    def clicked_release(self):
        self.trackList.clear()

        # set the album search string
        temp = self.albumList.selectedItems()
        # temporary obj used to access qtitem data, it's dumb
        self.master_query.album = temp[0].data(0)

    # this populates the tracklist widget
    @Slot()
    def call_mb_release_id(self):

        self.master_query.show_tracks()
        for item in self.master_query.MB_track_listing['recording-list']:
            QtWidgets.QListWidgetItem(item['title'], self.trackList)

    # this writes the audacity compatible label track file
    @Slot()
    def write_label_track(self):
        self.master_query.write_label_track()


# this is the main loop
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    # this is how qt handles the window interaction
    widget = MainWindow()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
