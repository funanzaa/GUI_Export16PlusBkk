from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit
from export import Ui_export


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setEnabled(True)
        Login.resize(687, 327)
        Login.setMinimumSize(QtCore.QSize(687, 327))
        Login.setMaximumSize(QtCore.QSize(687, 327))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/User.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Login.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(275, 11, 401, 281))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Pass.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Login)  # Login

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 0, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password) # Set lineedit show password
        self.gridLayout.addWidget(self.lineEdit_password, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 201, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/desktop_computers.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("Please Enter Username & Password", 2000)
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def Login(self):
        username = self.lineEdit_username.text()
        passwd = self.lineEdit_password.text()

        if username == 'admin' and passwd == 'demo':
            # self.statusbar.showMessage("Go")
            self.form_export = QtWidgets.QMainWindow()
            self.ui = Ui_export()
            self.ui.setupUi(self.form_export)
            self.form_export.show() # show login
            Login.hide() #

        else:
            self.statusbar.showMessage("Username & Password is Wrong", 2000)


    # def closescr(self,):
    #     Login.hide()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.groupBox.setTitle(_translate("Login", "LogIn"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.lineEdit_username.setPlaceholderText(_translate("Login", "Username"))
        self.lineEdit_password.setPlaceholderText(_translate("Login", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())