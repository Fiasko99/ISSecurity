from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Send_OrderWindow(object):
    def setupUi(self, Send_OrderWindow):
        Send_OrderWindow.setObjectName("Send_OrderWindow")
        Send_OrderWindow.resize(800, 350)
        Send_OrderWindow.setMinimumSize(QtCore.QSize(800, 350))
        Send_OrderWindow.setMaximumSize(QtCore.QSize(800, 350))
        Send_OrderWindow.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"Color: rgb(85, 85, 255);\n"
"font: 63 12pt Lucida Sans;\n"
"margin: 2px;\n"
"border: 1px solid blue;")
        self.centralwidget = QtWidgets.QWidget(Send_OrderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.daterel_label = QtWidgets.QLabel(self.centralwidget)
        self.daterel_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.daterel_label.setObjectName("daterel_label")
        self.gridLayout_2.addWidget(self.daterel_label, 3, 0, 1, 1)
        self.note_label = QtWidgets.QLabel(self.centralwidget)
        self.note_label.setStyleSheet("margin-top: 85px;\n"
"margin-bottom: 85px;\n"
"background-color: rgb(255, 255, 127);")
        self.note_label.setObjectName("note_label")
        self.gridLayout_2.addWidget(self.note_label, 2, 0, 1, 1)
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.address.setObjectName("address")
        self.gridLayout_2.addWidget(self.address, 1, 1, 1, 1)
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.address_label.setObjectName("address_label")
        self.gridLayout_2.addWidget(self.address_label, 1, 0, 1, 1)
        self.note = QtWidgets.QTextEdit(self.centralwidget)
        self.note.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.note.setObjectName("note")
        self.gridLayout_2.addWidget(self.note, 2, 1, 1, 1)
        self.security_label = QtWidgets.QLabel(self.centralwidget)
        self.security_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.security_label.setObjectName("security_label")
        self.gridLayout_2.addWidget(self.security_label, 0, 0, 1, 1)
        self.date_exp = QtWidgets.QLineEdit(self.centralwidget)
        self.date_exp.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.date_exp.setObjectName("date_exp")
        self.gridLayout_2.addWidget(self.date_exp, 4, 1, 1, 1)
        self.dateexp_label = QtWidgets.QLabel(self.centralwidget)
        self.dateexp_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.dateexp_label.setObjectName("dateexp_label")
        self.gridLayout_2.addWidget(self.dateexp_label, 4, 0, 1, 1)
        self.send_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_btn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"margin: 20px;")
        self.send_btn.setObjectName("send_btn")
        self.gridLayout_2.addWidget(self.send_btn, 6, 0, 1, 2)
        self.sort_security = QtWidgets.QComboBox(self.centralwidget)
        self.sort_security.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.sort_security.setObjectName("sort_security")
        self.sort_security.addItem("")
        self.gridLayout_2.addWidget(self.sort_security, 0, 1, 1, 1)
        self.date_rel = QtWidgets.QLineEdit(self.centralwidget)
        self.date_rel.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.date_rel.setObjectName("date_rel")
        self.gridLayout_2.addWidget(self.date_rel, 3, 1, 1, 1)
        self.pay_label = QtWidgets.QLabel(self.centralwidget)
        self.pay_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pay_label.setObjectName("pay_label")
        self.gridLayout_2.addWidget(self.pay_label, 5, 0, 1, 1)
        self.pay_month = QtWidgets.QLineEdit(self.centralwidget)
        self.pay_month.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pay_month.setObjectName("pay_month")
        self.gridLayout_2.addWidget(self.pay_month, 5, 1, 1, 1)
        Send_OrderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Send_OrderWindow)
        QtCore.QMetaObject.connectSlotsByName(Send_OrderWindow)

    def retranslateUi(self, Send_OrderWindow):
        _translate = QtCore.QCoreApplication.translate
        Send_OrderWindow.setWindowTitle(_translate("Send_OrderWindow", "Окно заказа"))
        self.daterel_label.setText(_translate("Send_OrderWindow", "Дата выхода на работу"))
        self.note_label.setText(_translate("Send_OrderWindow", "Заметка"))
        self.address_label.setText(_translate("Send_OrderWindow", "Адрес"))
        self.security_label.setText(_translate("Send_OrderWindow", "Сотрудник"))
        self.dateexp_label.setText(_translate("Send_OrderWindow", "Дата окончания контракта"))
        self.send_btn.setText(_translate("Send_OrderWindow", "Оформить заказ"))
        self.sort_security.setItemText(0, _translate("Send_OrderWindow", "Выбрать"))
        self.pay_label.setText(_translate("Send_OrderWindow", "Месячная плата"))


