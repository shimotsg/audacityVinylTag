# 2/27/2020
# geoffrey shimotsu
# create dialog windows for user input to filter MBID query
# and display album choices

import PyQt5
from PyQt5 import QtGui
import sys

# uArtist, ok = PyQt5.QInputDialog.getText(self, )

# getText(self, window title, label before LineEdit widget)

# application def with sysargv to pass command line arguements to the application
# app = QtGui.QGuiApplication(sys.argv)

class Window(QtGui.QWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setTitle("VinylTag")
        # self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.show()

app = QtGui.QGuiApplication(sys.argv)
# window.setGeometry(0, 0, 500, 300)
GUI = Window()
sys.exit(app.exec_())
# name, ok = QtGui.QInputEvent.getText(window, 'Artist and Album',
# 'Enter album:')