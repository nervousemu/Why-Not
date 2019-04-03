# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newCustomer.ui',
# licensing of 'newCustomer.ui' applies.
#
# Created: Mon Apr  1 15:29:27 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_newCustomerDialog(object):
    def setupUi(self, newCustomerDialog):
        newCustomerDialog.setObjectName("newCustomerDialog")
        newCustomerDialog.resize(1089, 759)
        self.buttonBox = QtWidgets.QDialogButtonBox(newCustomerDialog)
        self.buttonBox.setGeometry(QtCore.QRect(880, 710, 176, 27))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.firstLabel = QtWidgets.QLabel(newCustomerDialog)
        self.firstLabel.setGeometry(QtCore.QRect(80, 100, 81, 17))
        self.firstLabel.setObjectName("firstLabel")
        self.zipEdit = QtWidgets.QLineEdit(newCustomerDialog)
        self.zipEdit.setGeometry(QtCore.QRect(580, 280, 171, 27))
        self.zipEdit.setObjectName("zipEdit")
        self.notesEdit = QtWidgets.QTextEdit(newCustomerDialog)
        self.notesEdit.setGeometry(QtCore.QRect(70, 350, 781, 251))
        self.notesEdit.setTabChangesFocus(True)
        self.notesEdit.setObjectName("notesEdit")
        self.cityLabel = QtWidgets.QLabel(newCustomerDialog)
        self.cityLabel.setGeometry(QtCore.QRect(80, 250, 41, 17))
        self.cityLabel.setObjectName("cityLabel")
        self.zipLabel = QtWidgets.QLabel(newCustomerDialog)
        self.zipLabel.setGeometry(QtCore.QRect(590, 250, 51, 17))
        self.zipLabel.setObjectName("zipLabel")
        self.stateLabel = QtWidgets.QLabel(newCustomerDialog)
        self.stateLabel.setGeometry(QtCore.QRect(500, 250, 51, 17))
        self.stateLabel.setObjectName("stateLabel")
        self.lastLabel = QtWidgets.QLabel(newCustomerDialog)
        self.lastLabel.setGeometry(QtCore.QRect(410, 100, 81, 17))
        self.lastLabel.setObjectName("lastLabel")
        self.addressEdit = QtWidgets.QLineEdit(newCustomerDialog)
        self.addressEdit.setGeometry(QtCore.QRect(70, 200, 691, 27))
        self.addressEdit.setObjectName("addressEdit")
        self.streetLabel = QtWidgets.QLabel(newCustomerDialog)
        self.streetLabel.setGeometry(QtCore.QRect(80, 180, 131, 17))
        self.streetLabel.setObjectName("streetLabel")
        self.firstNameEdit = QtWidgets.QLineEdit(newCustomerDialog)
        self.firstNameEdit.setGeometry(QtCore.QRect(70, 130, 311, 27))
        self.firstNameEdit.setObjectName("firstNameEdit")
        self.lastNameEdit = QtWidgets.QLineEdit(newCustomerDialog)
        self.lastNameEdit.setGeometry(QtCore.QRect(400, 130, 361, 27))
        self.lastNameEdit.setObjectName("lastNameEdit")
        self.cityEdit = QtWidgets.QLineEdit(newCustomerDialog)
        self.cityEdit.setGeometry(QtCore.QRect(70, 280, 401, 27))
        self.cityEdit.setObjectName("cityEdit")
        self.stateEdit = QtWidgets.QLineEdit(newCustomerDialog)
        self.stateEdit.setGeometry(QtCore.QRect(490, 280, 71, 27))
        self.stateEdit.setObjectName("stateEdit")
        self.notesLabel = QtWidgets.QLabel(newCustomerDialog)
        self.notesLabel.setGeometry(QtCore.QRect(70, 330, 121, 17))
        self.notesLabel.setObjectName("notesLabel")
        self.titleLabel = QtWidgets.QLabel(newCustomerDialog)
        self.titleLabel.setGeometry(QtCore.QRect(300, 20, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.retranslateUi(newCustomerDialog)
        QtCore.QMetaObject.connectSlotsByName(newCustomerDialog)
        newCustomerDialog.setTabOrder(self.firstNameEdit, self.lastNameEdit)
        newCustomerDialog.setTabOrder(self.lastNameEdit, self.addressEdit)
        newCustomerDialog.setTabOrder(self.addressEdit, self.cityEdit)
        newCustomerDialog.setTabOrder(self.cityEdit, self.stateEdit)
        newCustomerDialog.setTabOrder(self.stateEdit, self.zipEdit)
        newCustomerDialog.setTabOrder(self.zipEdit, self.notesEdit)

    def retranslateUi(self, newCustomerDialog):
        newCustomerDialog.setWindowTitle(QtWidgets.QApplication.translate("newCustomerDialog", "New Customer", None, -1))
        self.firstLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "First Name:", None, -1))
        self.cityLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "City:", None, -1))
        self.zipLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "Zip", None, -1))
        self.stateLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "State:", None, -1))
        self.lastLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "Last Name:", None, -1))
        self.streetLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "Street Address:", None, -1))
        self.notesLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "Additional Notes:", None, -1))
        self.titleLabel.setText(QtWidgets.QApplication.translate("newCustomerDialog", "Enter Customer Information", None, -1))

