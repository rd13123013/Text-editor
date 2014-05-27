# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Tue May 27 12:55:07 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(800, 600)
        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.open_file = QtGui.QPushButton(self.centralwidget)
        self.open_file.setGeometry(QtCore.QRect(20, 10, 351, 51))
        self.open_file.setObjectName(_fromUtf8("open_file"))
        self.cancel = QtGui.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(400, 10, 351, 51))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.edit_window = QtGui.QTextEdit(self.centralwidget)
        self.edit_window.setGeometry(QtCore.QRect(0, 70, 831, 491))
        self.edit_window.setObjectName(_fromUtf8("edit_window"))
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        notepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(notepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        notepad.setStatusBar(self.statusbar)

        self.retranslateUi(notepad)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "MainWindow", None))
        self.open_file.setText(_translate("notepad", "Open File", None))
        self.cancel.setText(_translate("notepad", "Cancel", None))

