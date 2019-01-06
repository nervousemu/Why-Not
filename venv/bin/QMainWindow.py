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

appDataPath = os.path.expanduser("~") + "/Why-Not-Data/"

if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception:
        appDataPath = os.getcwd()


class MainWindow(QMainWindow, welcomeGui.Ui_mainWindow):

    dbPath = appDataPath + "customer.db"
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.newButton, SIGNAL("clicked()"), self.newCustomer)
        self.connect(self.openButton, SIGNAL("clicked()"), self.openCustomer)

        self.newCust = NewCustomerWindow()
        self.openCust = SearchCustomers()

        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, firstname TEXT,
        lastname TEXT, address TEXT, address2 TEXT, city TEXT, state TEXT, zip TEXT)""")
        self.dbConn.commit()
        self.dbConn.close()

    def newCustomer(self):
        self.newCust.open()

    def openCustomer(self):
        self.openCust.open()


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
        address2 = self.address2Edit.text()
        city = self.cityEdit.text()
        state = self.stateEdit.text()
        zip_code = self.zipEdit.text()

        # currentRowCount = self.mainTable.rowCount()
        #
        # self.mainTable.insertRow(currentRowCount)
        # self.mainTable.setItem(currentRowCount, 0, QTableWidgetItem(first_name))
        # self.mainTable.setItem(currentRowCount, 1, QTableWidgetItem(last_name))
        # self.mainTable.setItem(currentRowCount, 2, QTableWidgetItem(address))
        # self.mainTable.setItem(currentRowCount, 3, QTableWidgetItem(address2))
        # self.mainTable.setItem(currentRowCount, 4, QTableWidgetItem(city))
        # self.mainTable.setItem(currentRowCount, 5, QTableWidgetItem(state))
        # self.mainTable.setItem(currentRowCount, 6, QTableWidgetItem(zip_code))

        parameters = (None, first_name, last_name, address, address2, city, state, zip_code)
        self.dbCursor.execute('''INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', parameters)
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
        self.firstNameEdit.clear()
        self.lastNameEdit.clear()
        self.addressEdit.clear()
        self.address2Edit.clear()
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


class SearchCustomers(QDialog, customerSearchGui.Ui_searchDialog):

    def __init__(self, parent=None):
        super(SearchCustomers, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.searchCustomer)
        self.buttonBox.rejected.connect(self.cancelSearch)

    def searchCustomer(self):
        SearchCustomers.close(self)

    def cancelSearch(self):
        SearchCustomers.close(self)


app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
