from PyQt5.QtWidgets import *
from PyQt5 import *
import sys


class msgBox:
    def info(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Information")
        msg.setText(text)
        # msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
