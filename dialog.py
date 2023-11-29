# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(3820, 2135)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 932, 1055))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.mapFrame = QLabel(self.frame)
        self.mapFrame.setObjectName(u"mapFrame")
        self.mapFrame.setGeometry(QRect(0, 0, 932, 1055))
        self.graphFrame = QLabel(Dialog)
        self.graphFrame.setObjectName(u"graphFrame")
        self.graphFrame.setGeometry(QRect(950, 44, 951, 1011))
        self.graphFrame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleFrame = QLabel(Dialog)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(951, 0, 951, 40))
        self.fotosFrame = QLabel(Dialog)
        self.fotosFrame.setObjectName(u"fotosFrame")
        self.fotosFrame.setGeometry(QRect(950, 560, 951, 495))
        self.fotosFrame.setAlignment(Qt.AlignCenter)
        self.frame.raise_()
        self.titleFrame.raise_()
        self.fotosFrame.raise_()
        self.graphFrame.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.mapFrame.setText("")
        self.graphFrame.setText("")
        self.titleFrame.setText("")
        self.fotosFrame.setText("")
    # retranslateUi

