from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import sys

import welcomeGui
import newGui


class MainWindow(QMainWindow, welcomeGui.Ui_mainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.newCustomer = NewCustomerWindow()
        self.newButton.clicked.connect(self.newbuttonclicked)

    def newbuttonclicked(self):
        pass


class NewCustomerWindow(QDialog, newGui.Ui_newCustomerDialog):

    def __init__(self, parent=None):
        super(NewCustomerWindow, self).__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()