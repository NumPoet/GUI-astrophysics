import sys
from PyQt4 import QtGui
from colhypod import Ui_colhypod


class GUIcolhypod(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_colhypod()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUIcolhypod()
    myapp.show()
    sys.exit(app.exec_())
