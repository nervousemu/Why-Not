# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customerSearch.ui',
# licensing of 'customerSearch.ui' applies.
#
# Created: Wed Nov 21 18:49:51 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_searchDialog(object):
    def setupUi(self, searchDialog):
        searchDialog.setObjectName("searchDialog")
        searchDialog.resize(1024, 549)
        self.label = QtWidgets.QLabel(searchDialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 301, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(searchDialog)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(searchDialog)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(searchDialog)
        self.label_4.setGeometry(QtCore.QRect(70, 200, 68, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(searchDialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 100, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(searchDialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 170, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(searchDialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 230, 113, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.listView = QtWidgets.QListView(searchDialog)
        self.listView.setGeometry(QtCore.QRect(520, 40, 401, 401))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(searchDialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 290, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.buttonBox = QtWidgets.QDialogButtonBox(searchDialog)
        self.buttonBox.setGeometry(QtCore.QRect(830, 510, 176, 27))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(searchDialog)
        QtCore.QMetaObject.connectSlotsByName(searchDialog)

    def retranslateUi(self, searchDialog):
        searchDialog.setWindowTitle(QtWidgets.QApplication.translate("searchDialog", "Search For Customer", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("searchDialog", "Enter the information to lookup customer", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("searchDialog", "First Name:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("searchDialog", "Last Name:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("searchDialog", "Address:", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("searchDialog", "Search", None, -1))

