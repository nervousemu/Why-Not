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
import QNewCustomer
import QSearchCustomers

appDataPath = os.path.expanduser("~") + "/Why-Not-Data/"
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

        # self.newCust = QNewCustomer()
        # self.openCust = SearchCustomers()

        self.actionExit.triggered.connect(self.exit_action_triggered)

        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, firstname TEXT,
        lastname TEXT, address TEXT, city TEXT, state TEXT, zip TEXT)""")
        self.dbConn.commit()

    def newCustomer(self):
        # QNewCustomer.NewCustomerWindow(self)
        pass

    def openCustomer(self):
        # QSearchCustomers
        pass

    def exit_action_triggered(self):
        self.close


app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
