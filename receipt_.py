# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receipt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_receipt_window(object):
    def openwindow(self, receipt_window):
        from user_screen_ import Ui_user_scr
        self.b_window = QtWidgets.QMainWindow()
        self.ui = Ui_user_scr()
        self.ui.setupUi(self.b_window)
        self.b_window.show()
        receipt_window.close()

    def setupUi(self, receipt_window):
        receipt_window.setObjectName("receipt_window")
        receipt_window.resize(403, 600)
        self.centralwidget = QtWidgets.QWidget(receipt_window)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 401, 601))
        self.background.setStyleSheet("QLabel\n"
"{\n"
"    background-color: white;\n"
"}")
        self.background.setText("")
        self.background.setObjectName("background")
        self.receipt = QtWidgets.QLabel(self.centralwidget)
        self.receipt.setGeometry(QtCore.QRect(70, 30, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.receipt.setFont(font)
        self.receipt.setAlignment(QtCore.Qt.AlignCenter)
        self.receipt.setObjectName("receipt")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(50, 100, 301, 20))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.day = QtWidgets.QLabel(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(30, 180, 68, 31))
        self.day.setObjectName("day")
        self.order_id = QtWidgets.QLabel(self.centralwidget)
        self.order_id.setGeometry(QtCore.QRect(30, 230, 71, 31))
        self.order_id.setObjectName("order_id")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(220, 180, 68, 31))
        self.date.setObjectName("date")
        self.order_name = QtWidgets.QLabel(self.centralwidget)
        self.order_name.setGeometry(QtCore.QRect(30, 280, 101, 31))
        self.order_name.setObjectName("order_name")
        self.food_items = QtWidgets.QLabel(self.centralwidget)
        self.food_items.setGeometry(QtCore.QRect(30, 330, 101, 31))
        self.food_items.setObjectName("food_items")
        self.diet_target = QtWidgets.QLabel(self.centralwidget)
        self.diet_target.setGeometry(QtCore.QRect(30, 380, 91, 31))
        self.diet_target.setObjectName("diet_target")
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(30, 430, 91, 31))
        self.total.setObjectName("total")
        self.address = QtWidgets.QLabel(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(30, 480, 101, 31))
        self.address.setObjectName("address")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(30, 130, 131, 31))
        self.name.setObjectName("name")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(270, 130, 31, 31))
        self.id.setObjectName("id")
        self.name_blank = QtWidgets.QLabel(self.centralwidget)
        self.name_blank.setGeometry(QtCore.QRect(160, 130, 101, 31))
        self.name_blank.setText("")
        self.name_blank.setObjectName("name_blank")
        self.day_blank = QtWidgets.QLabel(self.centralwidget)
        self.day_blank.setGeometry(QtCore.QRect(70, 180, 101, 31))
        self.day_blank.setText("")
        self.day_blank.setObjectName("day_blank")
        self.id_blank = QtWidgets.QLabel(self.centralwidget)
        self.id_blank.setGeometry(QtCore.QRect(300, 130, 101, 31))
        self.id_blank.setText("")
        self.id_blank.setObjectName("id_blank")
        self.date_blank = QtWidgets.QLabel(self.centralwidget)
        self.date_blank.setGeometry(QtCore.QRect(270, 180, 111, 31))
        self.date_blank.setText("")
        self.date_blank.setObjectName("date_blank")
        self.order_id_blank = QtWidgets.QLabel(self.centralwidget)
        self.order_id_blank.setGeometry(QtCore.QRect(110, 230, 161, 31))
        self.order_id_blank.setText("")
        self.order_id_blank.setObjectName("order_id_blank")
        self.order_name_blank = QtWidgets.QLabel(self.centralwidget)
        self.order_name_blank.setGeometry(QtCore.QRect(130, 280, 181, 31))
        self.order_name_blank.setText("")
        self.order_name_blank.setObjectName("order_name_blank")
        self.food_items_blank = QtWidgets.QLabel(self.centralwidget)
        self.food_items_blank.setGeometry(QtCore.QRect(130, 330, 251, 31))
        self.food_items_blank.setText("")
        self.food_items_blank.setObjectName("food_items_blank")
        self.diet_target_blank = QtWidgets.QLabel(self.centralwidget)
        self.diet_target_blank.setGeometry(QtCore.QRect(130, 380, 241, 31))
        self.diet_target_blank.setText("")
        self.diet_target_blank.setObjectName("diet_target_blank")
        self.total_blank = QtWidgets.QLabel(self.centralwidget)
        self.total_blank.setGeometry(QtCore.QRect(120, 430, 251, 31))
        self.total_blank.setText("")
        self.total_blank.setObjectName("total_blank")
        self.address_blank = QtWidgets.QLabel(self.centralwidget)
        self.address_blank.setGeometry(QtCore.QRect(130, 480, 241, 31))
        self.address_blank.setText("")
        self.address_blank.setObjectName("address_blank")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openwindow(receipt_window))
        self.EXIT.setGeometry(QtCore.QRect(150, 530, 112, 34))
        self.EXIT.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: #f70202;\n"
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
        self.EXIT.setObjectName("EXIT")
        receipt_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(receipt_window)
        QtCore.QMetaObject.connectSlotsByName(receipt_window)

    def retranslateUi(self, receipt_window):
        _translate = QtCore.QCoreApplication.translate
        receipt_window.setWindowTitle(_translate("receipt_window", "MainWindow"))
        self.receipt.setText(_translate("receipt_window", "RECEIPT"))
        self.title.setText(_translate("receipt_window", "ATHLEAN FIT"))
        self.day.setText(_translate("receipt_window", "Day:"))
        self.order_id.setText(_translate("receipt_window", "Order-ID:"))
        self.date.setText(_translate("receipt_window", "Date:"))
        self.order_name.setText(_translate("receipt_window", "Order-Name:"))
        self.food_items.setText(_translate("receipt_window", "Food-Items:"))
        self.diet_target.setText(_translate("receipt_window", "Diet-Target:"))
        self.total.setText(_translate("receipt_window", "Total-Price:"))
        self.address.setText(_translate("receipt_window", "Address(To):"))
        self.name.setText(_translate("receipt_window", "Customer-Name:"))
        self.id.setText(_translate("receipt_window", "ID:"))
        self.EXIT.setText(_translate("receipt_window", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    receipt_window = QtWidgets.QMainWindow()
    ui = Ui_receipt_window()
    ui.setupUi(receipt_window)
    receipt_window.show()
    sys.exit(app.exec_())