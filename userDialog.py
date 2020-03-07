# 2/27/2020
# geoffrey shimotsu
# create dialog windows for user input to filter MBID query
# and display album choices

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

import sys
import query



# uArtist, ok = PyQt5.QInputDialog.getText(self, )

# getText(self, window title, label before LineEdit widget)

# application def with sysargv to pass command line arguements to the application
# app = QtGui.QGuiApplication(sys.argv)

class Window(QtGui.QWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setTitle("VinylTag")
        layout = QtWidgets.QFormLayout
        # layout.addChildWidget(layout)

        # self.
        # self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        # populate dropdown with query results
        queryResults = []

        self.show()




app = QtGui.QGuiApplication(sys.argv)
GUI = Window()

# loadedQuery  = QtWidgets.

# userQuery = QtXmlPatterns.QXmlQuery
# userQuery.setQuery('')
# userQuery.bindVariable("artist", )
# userQuery.bindVariable("album",)
sys.exit(app.exec_())