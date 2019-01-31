from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import sys
import os
import logging

import welcomeGui
import newCustGui
import customerSearchGui
import sqlite3
import QMainWindow
import QSearchCustomers

appDataPath = os.path.expanduser("~") + "/Why-Not-Data/"
# This line serves no purpose

if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception:
        appDataPath = os.getcwd()


class NewCustomerWindow(QDialog, newCustGui.Ui_newCustomerDialog):

    dbPath = appDataPath + "customer.db"
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, parent=None):
        super(NewCustomerWindow, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.addCustomer)
        self.buttonBox.rejected.connect(self.cancelAdd)
        self.dbCursor = self.dbConn.cursor()

    def addCustomer(self):
        """Adds customer information to database. Clears form afterwords."""
        first_name = self.firstNameEdit.text()
        last_name = self.lastNameEdit.text()
        address = self.addressEdit.text()
        city = self.cityEdit.text()
        state = self.stateEdit.text()
        zip_code = self.zipEdit.text()

        parameters = (None, first_name, last_name, address, city, state, zip_code)
        self.dbCursor.execute('''INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?)''', parameters)
        self.dbConn.commit()

        self.clearForm()
        NewCustomerWindow.close(self)

    def cancelAdd(self):
        """Cancel current customer input and closes and clears form"""
        yes = QMessageBox.Yes
        msgBox = QMessageBox.question(self, "Why Not", "Information added will not be saved, continue?", yes
                                      , QMessageBox.No)
        if msgBox == yes:
            self.clearForm()
            NewCustomerWindow.close(self)

    def clearForm(self):
        """Clears all of the text edits and check boxes on the new customer form."""
        """This line means nothing"""
        self.firstNameEdit.clear()
        self.lastNameEdit.clear()
        self.addressEdit.clear()
        self.cityEdit.clear()
        self.stateEdit.clear()
        self.zipEdit.clear()
        self.soffitCheck.setChecked(False)
        self.roofCheck.setChecked(False)
        self.guttersCheck.setChecked(False)
        self.sidingCheck.setChecked(False)
        self.downspotCheck.setChecked(False)
        self.kitchenCheck.setChecked(False)
        self.deckCheck.setChecked(False)
        self.electricalCheck.setChecked(False)
        self.houseTypeEdit.clear()
        self.costEdit.clear()
        self.notesEdit.clear()


# app = QApplication.instance()
# if app is None:
#     app = QApplication(sys.argv)
# form = NewCustomerWindow()
# form.show()
# app.exec_()
