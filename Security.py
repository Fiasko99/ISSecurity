from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecurityWindow(object):
    def setupUi(self, SecurityWindow):
        SecurityWindow.setObjectName("SecurityWindow")
        SecurityWindow.resize(739, 257)
        SecurityWindow.setStyleSheet("background-color: rgb(255, 252, 155);\n"
"border: 1px solid blue;\n"
"font: 63 12pt Lucida Sans;\n"
"color: rgb(85, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(SecurityWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 0, 0, 1, 1)
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_input.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.login_input.setObjectName("login_input")
        self.gridLayout.addWidget(self.login_input, 0, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.email_input.setObjectName("email_input")
        self.gridLayout.addWidget(self.email_input, 2, 1, 1, 1)
        self.phone_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.phone_label.setObjectName("phone_label")
        self.gridLayout.addWidget(self.phone_label, 3, 0, 1, 1)
        self.phone_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_input.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.phone_input.setObjectName("phone_input")
        self.gridLayout.addWidget(self.phone_input, 3, 1, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin: 20px;")
        self.save_btn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.save_btn, 4, 0, 1, 2)
        SecurityWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecurityWindow)
        QtCore.QMetaObject.connectSlotsByName(SecurityWindow)

    def retranslateUi(self, SecurityWindow):
        _translate = QtCore.QCoreApplication.translate
        SecurityWindow.setWindowTitle(_translate("SecurityWindow", "Добавить охранника"))
        self.login_label.setText(_translate("SecurityWindow", "Введите инициалы охранника (Имя Фамилия):"))
        self.password_label.setText(_translate("SecurityWindow", "Пароль:"))
        self.email_label.setText(_translate("SecurityWindow", "email"))
        self.phone_label.setText(_translate("SecurityWindow", "Мобильный телефон"))
        self.save_btn.setText(_translate("SecurityWindow", "Сохранить"))
