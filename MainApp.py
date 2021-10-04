from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from login import Ui_Login


class AppWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

app = QApplication(sys.argv)
Note = AppWindow()
sys.exit(app.exec())