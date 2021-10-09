from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from login import Ui_Login
from export import Ui_export

class AppWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.Login)  # Login

    def Login(self):
        username = self.lineEdit_username.text()
        passwd = self.lineEdit_password.text()

        if username == 'admin' and passwd == 'demo':
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_export()
            self.ui.setupUi(self.window)
            self.window.show()
            self.hide()
            # self.export = QtWidgets.QMainWindow()
            # self.ui = Ui_export()
            # self.ui.setupUi(self.export)
            # self.form_export.show() # show login
            # self.hide() # hide login

        else:
            self.statusbar.showMessage("Username & Password is Wrong", 2000)


app = QApplication(sys.argv)
Note = AppWindow()
sys.exit(app.exec())