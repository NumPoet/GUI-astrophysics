# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colhypod.ui'
#
# Created: Wed Apr 18 23:36:11 2018
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_colhypod(object):
    def setupUi(self, colhypod):
        colhypod.setObjectName(_fromUtf8("colhypod"))
        colhypod.resize(760, 524)
        self.centralWidget = QtGui.QWidget(colhypod)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 19, 371, 441))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.graphicsView = QtGui.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 351, 421))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.frame_2 = QtGui.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(370, 19, 361, 441))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.widget = QtGui.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 10, 341, 421))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolBoxGraphics = QtGui.QToolBox(self.widget)
        self.toolBoxGraphics.setObjectName(_fromUtf8("toolBoxGraphics"))
        self.page_11 = QtGui.QWidget()
        self.page_11.setGeometry(QtCore.QRect(0, 0, 167, 391))
        self.page_11.setObjectName(_fromUtf8("page_11"))
        self.plotButton = QtGui.QPushButton(self.page_11)
        self.plotButton.setGeometry(QtCore.QRect(0, 0, 151, 41))
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.toolBoxGraphics.addItem(self.page_11, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.toolBoxGraphics)
        self.toolBoxOthers = QtGui.QToolBox(self.widget)
        self.toolBoxOthers.setObjectName(_fromUtf8("toolBoxOthers"))
        self.page_17 = QtGui.QWidget()
        self.page_17.setGeometry(QtCore.QRect(0, 0, 166, 391))
        self.page_17.setObjectName(_fromUtf8("page_17"))
        self.toolBoxOthers.addItem(self.page_17, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.toolBoxOthers)
        colhypod.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(colhypod)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 760, 19))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuColhypod = QtGui.QMenu(self.menuBar)
        self.menuColhypod.setObjectName(_fromUtf8("menuColhypod"))
        colhypod.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(colhypod)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        colhypod.addToolBar(QtCore.Qt.LeftToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(colhypod)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        colhypod.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuColhypod.menuAction())

        self.retranslateUi(colhypod)
        self.toolBoxGraphics.setCurrentIndex(0)
        self.toolBoxOthers.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(colhypod)

    def retranslateUi(self, colhypod):
        colhypod.setWindowTitle(_translate("colhypod", "colhypod", None))
        self.plotButton.setText(_translate("colhypod", "Plotter", None))
        self.toolBoxGraphics.setItemText(self.toolBoxGraphics.indexOf(self.page_11), _translate("colhypod", "Graphing tools", None))
        self.toolBoxOthers.setItemText(self.toolBoxOthers.indexOf(self.page_17), _translate("colhypod", "Other tools", None))
        self.menuColhypod.setTitle(_translate("colhypod", "Colhypod", None))

