# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Wed Apr  6 12:50:31 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1900, 1055)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 932, 1055))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mapFrame = QtGui.QLabel(self.frame)
        self.mapFrame.setGeometry(QtCore.QRect(0, 0, 932, 1055))
        self.mapFrame.setText("")
        self.mapFrame.setObjectName("mapFrame")
        self.graphFrame = QtGui.QLabel(Dialog)
        self.graphFrame.setGeometry(QtCore.QRect(950, 44, 951, 1011))
        self.graphFrame.setText("")
        self.graphFrame.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphFrame.setObjectName("graphFrame")
        self.titleFrame = QtGui.QLabel(Dialog)
        self.titleFrame.setGeometry(QtCore.QRect(951, 0, 951, 40))
        self.titleFrame.setText("")
        self.titleFrame.setObjectName("titleFrame")
        self.fotosFrame = QtGui.QLabel(Dialog)
        self.fotosFrame.setGeometry(QtCore.QRect(950, 560, 951, 495))
        self.fotosFrame.setText("")
        self.fotosFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.fotosFrame.setObjectName("fotosFrame")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

