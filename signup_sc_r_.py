# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_scr.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Conn_database import *


class Ui_signup_scr(object):

    def openwindow(self, signup_scr):
        if self.name.text() != '' and self.user_id.text() != '' and self.password.text() != '' and self.age.text() != '' and self.weight.text() != '' and self.address.text() != '' and self.email.text() != '' and self.phone_number.text() != '' and (self.vegetarian.isChecked() or self.pescatarian.isChecked() or self.keto.isChecked() or self.buff.isChecked() or self.lean.isChecked()) and (self.yes.isChecked() or self.no.isChecked()):
                name = self.name.text()
                user_id = self.user_id.text()
                password = self.password.text()
                age = self.age.text()
                weight = self.weight.text()
                address = self.address.text()
                email = self.email.text()
                phone_number = self.phone_number.text()

                print(type(phone_number))

                if self.vegetarian.isChecked():
                        food_pref = 'vegetarian'
                elif self.pescatarian.isChecked():
                        food_pref = 'pescatarian'
                elif self.keto.isChecked():
                        food_pref = 'keto'
                elif self.lean.isChecked():
                        food_pref = 'lean' 
                elif self.buff.isChecked():
                        food_pref = 'buff'
                else:
                        food_pref = 'none'

                if self.yes.isChecked():
                        if(insert_trainer(user_id, name, password, int(age), address, email, int(phone_number))):
                                from login_ import Ui_login_scr
                                self.b_window = QtWidgets.QMainWindow()
                                self.ui = Ui_login_scr()
                                self.ui.setupUi(self.b_window)
                                self.b_window.show()
                                signup_scr.close()
                        else:
                                pass
                elif self.no.isChecked():
                        if(insert_user(user_id, name, password, int(age), int(weight), address, email, int(phone_number), food_pref)):
                                #id,name,password,age,weight,address,email,phone,foodpref
                                from login_ import Ui_login_scr
                                self.b_window = QtWidgets.QMainWindow()
                                self.ui = Ui_login_scr()
                                self.ui.setupUi(self.b_window)
                                self.b_window.show()
                                signup_scr.close()
                        else:
                                pass
        else:
                pass
    def setupUi(self, signup_scr):
        signup_scr.setObjectName("signup_scr")
        signup_scr.resize(531, 797)
        self.centralwidget = QtWidgets.QWidget(signup_scr)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -2, 531, 801))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.background.setFont(font)
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/images/image_2.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.user_id = QtWidgets.QLineEdit(self.centralwidget)
        self.user_id.setGeometry(QtCore.QRect(30, 140, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.user_id.setFont(font)
        self.user_id.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.user_id.setObjectName("user_id")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(30, 210, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.password.setObjectName("password")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(30, 280, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.age.setFont(font)
        self.age.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.age.setObjectName("age")
        self.weight = QtWidgets.QLineEdit(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(30, 350, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.weight.setFont(font)
        self.weight.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.weight.setObjectName("weight")
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(30, 420, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.address.setFont(font)
        self.address.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.address.setObjectName("address")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(30, 490, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.email.setObjectName("email")
        self.phone_number = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_number.setGeometry(QtCore.QRect(30, 560, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.phone_number.setFont(font)
        self.phone_number.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.phone_number.setObjectName("phone_number")
        self.trainer_q = QtWidgets.QLabel(self.centralwidget)
        self.trainer_q.setGeometry(QtCore.QRect(290, 70, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.trainer_q.setFont(font)
        self.trainer_q.setStyleSheet("QLabel\n"
"{\n"
"    color: white;\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"}")
        self.trainer_q.setObjectName("trainer_q")
        self.yes = QtWidgets.QRadioButton(self.centralwidget)
        self.yes.setGeometry(QtCore.QRect(290, 140, 119, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yes.setFont(font)
        self.yes.setStyleSheet("QRadioButton\n"
"{\n"
"    color: white;\n"
"}")
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QRadioButton(self.centralwidget)
        self.no.setGeometry(QtCore.QRect(290, 180, 119, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.no.setFont(font)
        self.no.setStyleSheet("QRadioButton\n"
"{\n"
"    color: white;\n"
"}")
        self.no.setObjectName("no")
        self.food_pref = QtWidgets.QLabel(self.centralwidget)
        self.food_pref.setGeometry(QtCore.QRect(290, 210, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.food_pref.setFont(font)
        self.food_pref.setStyleSheet("QLabel\n"
"{\n"
"    color: white;\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"}")
        self.food_pref.setObjectName("food_pref")
        self.sign_up = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openwindow(signup_scr))
        self.sign_up.setGeometry(QtCore.QRect(80, 653, 371, 61))
        self.sign_up.setStyleSheet("QPushButton {\n"
"    border: 1px solid white;\n"
"    border-radius: 25px;\n"
"    background-color: #03a9fc;\n"
"    min-width: 80px;\n"
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
        self.sign_up.setObjectName("sign_up")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(30, 70, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setStyleSheet("QLineEdit {\n"
"    border-bottom: 2px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background : transparent;\n"
"    color: white;\n"
"}")
        self.name.setObjectName("name")
        self.vegetarian = QtWidgets.QCheckBox(self.centralwidget)
        self.vegetarian.setGeometry(QtCore.QRect(290, 290, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vegetarian.setFont(font)
        self.vegetarian.setStyleSheet("QCheckBox\n"
"{\n"
"    color: white;\n"
"}")
        self.vegetarian.setObjectName("vegetarian")
        self.pescatarian = QtWidgets.QCheckBox(self.centralwidget)
        self.pescatarian.setGeometry(QtCore.QRect(290, 330, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pescatarian.setFont(font)
        self.pescatarian.setStyleSheet("QCheckBox\n"
"{\n"
"    color: white;\n"
"}")
        self.pescatarian.setObjectName("pescatarian")
        self.keto = QtWidgets.QCheckBox(self.centralwidget)
        self.keto.setGeometry(QtCore.QRect(290, 370, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keto.setFont(font)
        self.keto.setStyleSheet("QCheckBox\n"
"{\n"
"    color: white;\n"
"}")
        self.keto.setObjectName("keto")
        self.lean = QtWidgets.QCheckBox(self.centralwidget)
        self.lean.setGeometry(QtCore.QRect(290, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lean.setFont(font)
        self.lean.setStyleSheet("QCheckBox\n"
"{\n"
"    color: white;\n"
"}")
        self.lean.setObjectName("lean")
        self.buff = QtWidgets.QCheckBox(self.centralwidget)
        self.buff.setGeometry(QtCore.QRect(290, 450, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buff.setFont(font)
        self.buff.setStyleSheet("QCheckBox\n"
"{\n"
"    color: white;\n"
"}")
        self.buff.setObjectName("buff")
        signup_scr.setCentralWidget(self.centralwidget)

        self.retranslateUi(signup_scr)
        QtCore.QMetaObject.connectSlotsByName(signup_scr)

    def retranslateUi(self, signup_scr):
        _translate = QtCore.QCoreApplication.translate
        signup_scr.setWindowTitle(_translate("signup_scr", "MainWindow"))
        self.user_id.setText(_translate("signup_scr", "Username"))
        self.password.setText(_translate("signup_scr", "Password"))
        self.age.setText(_translate("signup_scr", "Age"))
        self.weight.setText(_translate("signup_scr", "Weight"))
        self.address.setText(_translate("signup_scr", "Address"))
        self.email.setText(_translate("signup_scr", "Email"))
        self.phone_number.setText(_translate("signup_scr", "Phone Number"))
        self.trainer_q.setText(_translate("signup_scr", "Applying for trainer?"))
        self.yes.setText(_translate("signup_scr", "Yes"))
        self.no.setText(_translate("signup_scr", "No"))
        self.food_pref.setText(_translate("signup_scr", "Food Preference"))
        self.sign_up.setText(_translate("signup_scr", "SIGN UP"))
        self.name.setText(_translate("signup_scr", "Name"))
        self.vegetarian.setText(_translate("signup_scr", "Vegetarian"))
        self.pescatarian.setText(_translate("signup_scr", "Pescatarian"))
        self.keto.setText(_translate("signup_scr", "Keto"))
        self.lean.setText(_translate("signup_scr", "Lean Diet"))
        self.buff.setText(_translate("signup_scr", "Buff Diet"))
import app_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signup_scr = QtWidgets.QMainWindow()
    ui = Ui_signup_scr()
    ui.setupUi(signup_scr)
    signup_scr.show()
    sys.exit(app.exec_())
