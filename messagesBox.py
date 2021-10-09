from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class msgBox:

    def info(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()