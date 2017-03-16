# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Wed Mar 15 22:51:39 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(380, 80, 932, 1055))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mapFrame = QtGui.QLabel(self.frame)
        self.mapFrame.setGeometry(QtCore.QRect(0, 0, 932, 1055))
        self.mapFrame.setText("")
        self.mapFrame.setObjectName("mapFrame")
        self.titleFrame = QtGui.QLabel(self.centralwidget)
        self.titleFrame.setGeometry(QtCore.QRect(1331, 80, 951, 40))
        self.titleFrame.setText("")
        self.titleFrame.setObjectName("titleFrame")
        self.graphFrame = QtGui.QLabel(self.centralwidget)
        self.graphFrame.setGeometry(QtCore.QRect(1330, 124, 951, 1011))
        self.graphFrame.setText("")
        self.graphFrame.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphFrame.setObjectName("graphFrame")
        self.fotosFrame = QtGui.QLabel(self.centralwidget)
        self.fotosFrame.setGeometry(QtCore.QRect(1330, 640, 951, 495))
        self.fotosFrame.setText("")
        self.fotosFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.fotosFrame.setObjectName("fotosFrame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

