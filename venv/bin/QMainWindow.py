from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import sys

import welcomeGui
import newCustGui
import sqlite3
conn = sqlite3.connect('customer.db')


class MainWindow(QMainWindow, welcomeGui.Ui_mainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.newButton, SIGNAL("clicked()"), self.newCustomer)

        self.newCust = NewCustomerWindow()

    def newCustomer(self):
        self.newCust.open()


class NewCustomerWindow(QDialog, newCustGui.Ui_newCustomerDialog):

    def __init__(self, parent=None):
        super(NewCustomerWindow, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.addCustomer)
        self.buttonBox.rejected.connect(self.cancelAdd)

    def addCustomer(self):
        firstName = self.firstNameEdit.text()
        lastName = self.lastNameEdit.text()
        address = self.addressEdit.text()
        address2 = self.address2Edit.text()
        city = self.cityEdit.text()
        state = self.stateEdit.text()
        zipCode = self.zipEdit.text()
        houseType = self.houseTypeEdit.text()
        jobCost = self.costEdit.text()
        soffit = self.soffitCheck
        roofing = self.roofCheck
        gutters = self.guttersCheck
        siding = self.sidingCheck
        downspot = self.downspotCheck
        kitchen = self.kitchenCheck
        deck = self.deckCheck
        electrical = self.electricalCheck

        dbEntry = [firstName, lastName, address, address2, city, state, zipCode]



        #for i in range(len(dbEntry)):
         #   print(dbEntry[i])

        #QMessageBox.information(self, "Why Not", str(firstName) + " has been added!")
        if soffit.isChecked():
            soffit.clear()
        if roofing.isChecked():
            pass
        if gutters.isChecked():
            pass
        if siding.isChecked():
            pass
        if downspot.isChecked():
            pass
        if kitchen.isChecked():
            pass
        if deck.isChecked():
            pass
        if electrical.isChecked():
            pass

        self.firstNameEdit.clear()
        NewCustomerWindow.close(self)

    def cancelAdd(self):
        yes = QMessageBox.Yes
        msgBox = QMessageBox.question(self, "Why Not", "Information added will not be saved, continue?", yes
                                      , QMessageBox.No)
        if msgBox == yes:
            NewCustomerWindow.close(self)

    def addToDB(self, dbEntry):
        for i in range(len(dbEntry)):
            print(dbEntry[i])
        #c = conn.cursor()
        #c.execute('''CREATE TABLE customers()''')


app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
