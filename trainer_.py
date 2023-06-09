# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
from Conn_database import *

class Ui_MainWindow(object):
    def openwindow(self, MainWindow, name):
        if name == 'exit':
            from login_ import Ui_login_scr
            self.b_window = QtWidgets.QMainWindow()
            self.ui = Ui_login_scr()
            self.ui.setupUi(self.b_window)
            self.b_window.show()
            MainWindow.close()

        elif name == 'cash':
            self.wallet_blank.setText('0')
            self.dialogue.setText('SENT')

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 471, 601))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/image_5.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(230, 160, 21, 19))
        self.id.setObjectName("id")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(230, 190, 51, 19))
        self.name.setObjectName("name")
        self.hire_date = QtWidgets.QLabel(self.centralwidget)
        self.hire_date.setGeometry(QtCore.QRect(230, 220, 81, 19))
        self.hire_date.setObjectName("hire_date")
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(230, 250, 131, 19))
        self.total.setObjectName("total")
        self.salary = QtWidgets.QLabel(self.centralwidget)
        self.salary.setGeometry(QtCore.QRect(230, 280, 121, 19))
        self.salary.setObjectName("salary")
        self.wallet = QtWidgets.QLabel(self.centralwidget)
        self.wallet.setGeometry(QtCore.QRect(230, 310, 68, 19))
        self.wallet.setObjectName("wallet")
        self.id_blank = QtWidgets.QLabel(self.centralwidget)
        self.id_blank.setGeometry(QtCore.QRect(260, 160, 191, 19))
        self.id_blank.setText("")
        self.id_blank.setObjectName("id_blank")
        self.name_blank = QtWidgets.QLabel(self.centralwidget)
        self.name_blank.setGeometry(QtCore.QRect(290, 190, 171, 19))
        self.name_blank.setText("")
        self.name_blank.setObjectName("name_blank")
        self.hire_blank = QtWidgets.QLabel(self.centralwidget)
        self.hire_blank.setGeometry(QtCore.QRect(310, 220, 161, 19))
        self.hire_blank.setText("")
        self.hire_blank.setObjectName("hire_blank")
        self.total_blank = QtWidgets.QLabel(self.centralwidget)
        self.total_blank.setGeometry(QtCore.QRect(360, 250, 111, 20))
        self.total_blank.setText("")
        self.total_blank.setObjectName("total_blank")
        self.salary_blank = QtWidgets.QLabel(self.centralwidget)
        self.salary_blank.setGeometry(QtCore.QRect(350, 280, 111, 20))
        self.salary_blank.setText("")
        self.salary_blank.setObjectName("salary_blank")
        self.wallet_blank = QtWidgets.QLabel(self.centralwidget)
        self.wallet_blank.setGeometry(QtCore.QRect(290, 310, 171, 20))
        self.wallet_blank.setText("")
        self.wallet_blank.setObjectName("wallet_blank")
        self.exit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openwindow(MainWindow, 'exit'))
        self.exit.setGeometry(QtCore.QRect(180, 540, 112, 34))
        self.exit.setStyleSheet("QPushButton {\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"    background-color: red;\n"
"    min-width: 80px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.exit.setObjectName("exit")
        self.dialogue = QtWidgets.QLabel(self.centralwidget)
        self.dialogue.setGeometry(QtCore.QRect(200, 460, 81, 19))
        self.dialogue.setText("")
        self.dialogue.setAlignment(QtCore.Qt.AlignCenter)
        self.dialogue.setObjectName("dialogue")
        self.cashout = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openwindow(MainWindow, 'cash'))
        self.cashout.setGeometry(QtCore.QRect(280, 360, 112, 34))
        self.cashout.setStyleSheet("QPushButton {\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"    background-color: green;\n"
"    min-width: 80px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.cashout.setObjectName("cashout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.id.setText(_translate("MainWindow", "ID:"))
        self.name.setText(_translate("MainWindow", "Name:"))
        self.hire_date.setText(_translate("MainWindow", "Hire Date:"))
        self.total.setText(_translate("MainWindow", "Total Customers:"))
        self.salary.setText(_translate("MainWindow", "Monthly Salary: "))
        self.wallet.setText(_translate("MainWindow", "Wallet:"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.cashout.setText(_translate("MainWindow", "Cash Out"))
import app_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
