# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_kmloverlay_dockwidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_KMLOverlayDockWidget(object):
    def setupUi(self, KMLOverlayDockWidget):
        KMLOverlayDockWidget.setObjectName(_fromUtf8("KMLOverlayDockWidget"))
        KMLOverlayDockWidget.resize(649, 104)
        self.verticalLayout = QtGui.QVBoxLayout(KMLOverlayDockWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.cbOverlay = QtGui.QCheckBox(KMLOverlayDockWidget)
        self.cbOverlay.setObjectName(_fromUtf8("cbOverlay"))
        self.horizontalLayout_5.addWidget(self.cbOverlay)
        self.leFile = QtGui.QLineEdit(KMLOverlayDockWidget)
        self.leFile.setObjectName(_fromUtf8("leFile"))
        self.horizontalLayout_5.addWidget(self.leFile)
        self.btSelectFile = QtGui.QToolButton(KMLOverlayDockWidget)
        self.btSelectFile.setObjectName(_fromUtf8("btSelectFile"))
        self.horizontalLayout_5.addWidget(self.btSelectFile)
        self.btLoadFile = QtGui.QToolButton(KMLOverlayDockWidget)
        self.btLoadFile.setObjectName(_fromUtf8("btLoadFile"))
        self.horizontalLayout_5.addWidget(self.btLoadFile)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(KMLOverlayDockWidget)
        QtCore.QMetaObject.connectSlotsByName(KMLOverlayDockWidget)

    def retranslateUi(self, KMLOverlayDockWidget):
        KMLOverlayDockWidget.setWindowTitle(_translate("KMLOverlayDockWidget", "KML Overlay", None))
        self.cbOverlay.setText(_translate("KMLOverlayDockWidget", "KML Overlay", None))
        self.btSelectFile.setText(_translate("KMLOverlayDockWidget", "...", None))
        self.btLoadFile.setText(_translate("KMLOverlayDockWidget", "load", None))
