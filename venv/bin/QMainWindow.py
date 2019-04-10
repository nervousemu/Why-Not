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
import customerEdit

appDataPath = os.path.expanduser("~") + "/Why-Not-Data/"
print(appDataPath)
# This line serves no purpose

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

        # self.newCust = NewCustomerWindow()
        # self.openCust = SearchCustomers()

        self.actionExit.triggered.connect(self.exit_action_triggered)

        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, first_name TEXT,
        last_name TEXT, address TEXT, city TEXT, state TEXT, zip_code TEXT, notes TEXT)""")
        self.dbConn.commit()
        self.dbConn.close()

    def newCustomer(self):
        self.newCust = NewCustomerWindow()
        self.newCust.open()

    def openCustomer(self):
        self.openCust = SearchCustomers()
        self.openCust.open()

    def exit_action_triggered(self):
        self.close()


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
        adtl_info = self.notesEdit.toPlainText()

        # currentRowCount = self.mainTable.rowCount()
        #
        # self.mainTable.insertRow(currentRowCount)
        # self.mainTable.setItem(currentRowCount, 0, QTableWidgetItem(first_name))
        # self.mainTable.setItem(currentRowCount, 1, QTableWidgetItem(last_name))
        # self.mainTable.setItem(currentRowCount, 2, QTableWidgetItem(address))
        # self.mainTable.setItem(currentRowCount, 4, QTableWidgetItem(city))
        # self.mainTable.setItem(currentRowCount, 5, QTableWidgetItem(state))
        # self.mainTable.setItem(currentRowCount, 6, QTableWidgetItem(zip_code))

        parameters = (None, first_name, last_name, address, city, state, zip_code, adtl_info)
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
        self.cityEdit.clear()
        self.stateEdit.clear()
        self.zipEdit.clear()
        # self.soffitCheck.setChecked(False)
        # self.roofCheck.setChecked(False)
        # self.guttersCheck.setChecked(False)
        # self.sidingCheck.setChecked(False)
        # self.downspotCheck.setChecked(False)
        # self.kitchenCheck.setChecked(False)
        # self.deckCheck.setChecked(False)
        # self.electricalCheck.setChecked(False)
        # self.houseTypeEdit.clear()
        # self.costEdit.clear()
        self.notesEdit.clear()


class SearchCustomers(QDialog, customerSearchGui.Ui_searchDialog):

    dbPath = appDataPath + "customer.db"
    dbConn = sqlite3.connect(dbPath)
    print(appDataPath)

    def __init__(self, parent=None):
        super(SearchCustomers, self).__init__(parent)
        self.setupUi(self)

        self.dbCursor = self.dbConn.cursor()
        # self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY,
        #      first_name TEXT, last_name TEXT, address TEXT, city TEXT, state TEXT, zip_code TEXT)""")
        self.dbConn.commit()

        # row = self.mainTable.currentRow
        # column = self.mainTable.currentColumn
        # # self.ID = self.mainTable.item(row.text(), column.text())

        self.connect(self.searchButton, SIGNAL("clicked()"), self.searchCustomer)
        self.buttonBox.accepted.connect(self.openInfo)
        self.buttonBox.rejected.connect(self.cancelSearch)

        self.mainTable.cellDoubleClicked.connect(self.cell_was_clicked)

        # self.customerInfo = {'indx': 0, 'firstN': '', 'lastN': '', 'address': '', 'city': '', 'state': '', 'zip': ''}

        self.ID = ''

        self.load_initial_stuff()

    def load_initial_stuff(self):
        """Loads the initial settings, displays the customer list"""
        self.dbCursor.execute("""SELECT * FROM Customers""")
        allRows = self.dbCursor.fetchall()


        for row in allRows:
            inx = allRows.index(row)
            self.mainTable.insertRow(inx)
            self.mainTable.setItem(inx, 0, QTableWidgetItem(row[1]))
            self.mainTable.setItem(inx, 1, QTableWidgetItem(row[2]))
            self.mainTable.setItem(inx, 2, QTableWidgetItem(row[3]))
            self.mainTable.setItem(inx, 3, QTableWidgetItem(row[4]))
            self.mainTable.setItem(inx, 4, QTableWidgetItem(row[5]))
            self.mainTable.setItem(inx, 5, QTableWidgetItem(row[6]))
            print(allRows[inx])

    def cell_was_clicked(self, row, column):
        """extracts data in a cell that was double clicked"""
        print("Row %d and Column %d was clicked" % (row, column))
        turkey = self.mainTable.rowSpan(row, column)
        print(turkey)
        cell_data = self.mainTable.item(row, column)
        self.ID = cell_data
        print(self.ID.text())
        print(self.mainTable.item(row, 0))
        row_data = []
        # for i in row:
        #     print(i)

    def searchCustomer(self):
        first_name = self.firstNameEdit.text()
        last_name = self.lastNameEdit.text()
        address = self.addressEdit.text()
        city = self.cityEdit.text()
        state = self.stateEdit.text()
        zip_code = self.zipEdit.text()

        table_name = "Customers"
        column_2 = "first_name"
        column_3 = "last_name"
        column_4 = "address"
        column_5 = "city"
        column_6 = "state"
        column_7 = "zip_code"

        # self.dbCursor.execute('SELECT * FROM {tn} WHERE {cn}="{fn}"'.format(tn=table_name,
        # cn=column_2, fn=first_name))
        # self.dbCursor.execute('SELECT * FROM {tn} WHERE {c2}="{fn}" OR {c3}="{ln}"'.
        #                       format(tn=table_name, c2=column_2, c3=column_3, fn=first_name, ln=last_name))
        self.dbCursor.execute('SELECT * FROM {tn} WHERE {c2}="{fn}" OR {c3}="{ln}" OR {c4}="{ad}" OR {c5}="{ci}"'
                              'OR {c6}="{st}" OR {c7}="{zi}"'.format(tn=table_name, c2=column_2, c3=column_3,
                                                                  c4=column_4, c5=column_5, c6=column_6,
                                                                  c7=column_7, fn=first_name, ln=last_name,
                                                                  ad=address, ci=city, st=state, zi=zip_code))

        all_rows = self.dbCursor.fetchall()
        print('1):', all_rows)

        self.mainTable.clearContents()

        for row in all_rows:
            inx = all_rows.index(row)
            self.mainTable.insertRow(inx)
            self.mainTable.setItem(inx, 0, QTableWidgetItem(row[1]))
            self.mainTable.setItem(inx, 1, QTableWidgetItem(row[2]))
            self.mainTable.setItem(inx, 2, QTableWidgetItem(row[3]))
            self.mainTable.setItem(inx, 3, QTableWidgetItem(row[4]))
            self.mainTable.setItem(inx, 4, QTableWidgetItem(row[5]))
            self.mainTable.setItem(inx, 5, QTableWidgetItem(row[6]))


        # currentRowCount = self.mainTable.rowCount()
        # self.mainTable.insertRow(currentRowCount)
        # self.mainTable.setItem(currentRowCount, 0, QTableWidgetItem(first_name))
        # self.mainTable.setItem(currentRowCount, 1, QTableWidgetItem(last_name))
        # self.mainTable.setItem(currentRowCount, 2, QTableWidgetItem(address))
        # self.mainTable.setItem(currentRowCount, 3, QTableWidgetItem(city))
        # self.mainTable.setItem(currentRowCount, 4, QTableWidgetItem(state))
        # self.mainTable.setItem(currentRowCount, 5, QTableWidgetItem(zip_code))

    def openInfo(self):
        pass

    def cancelSearch(self):
        self.dbConn.close()
        SearchCustomers.close(self)


app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()