from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IS_main(object):
    def setupUi(self, IS_main):
        IS_main.setObjectName("IS_main")
        IS_main.resize(550, 450)
        IS_main.setMinimumSize(QtCore.QSize(550, 450))
        IS_main.setMaximumSize(QtCore.QSize(550, 450))
        IS_main.setStyleSheet("background-color: rgb(255, 255, 200);")
        self.centralwidget = QtWidgets.QWidget(IS_main)
        self.centralwidget.setObjectName("centralwidget")
        self.form_grid = QtWidgets.QWidget(self.centralwidget)
        self.form_grid.setGeometry(QtCore.QRect(50, 50, 451, 341))
        self.form_grid.setStyleSheet("QWidget {\n"
"    background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}")
        self.form_grid.setObjectName("form_grid")
        self.gridLayout = QtWidgets.QGridLayout(self.form_grid)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password_line = QtWidgets.QLineEdit(self.form_grid)
        self.password_line.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(170, 255, 255);\n"
"    Color: rgb(85, 85, 255);\n"
"    font: 63 12pt \"Lucida Sans\";\n"
"    margin-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.gridLayout.addWidget(self.password_line, 1, 1, 1, 1)
        self.login_line = QtWidgets.QLineEdit(self.form_grid)
        self.login_line.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(170, 255, 255);\n"
"    Color: rgb(85, 85, 255);\n"
"    font: 63 12pt \"Lucida Sans\";\n"
"    margin-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.login_line.setObjectName("login_line")
        self.gridLayout.addWidget(self.login_line, 0, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.form_grid)
        self.login_label.setStyleSheet("QLabel {\n"
"    Color: rgb(85, 85, 255);\n"
"    font: 63 12pt \"Lucida Sans\";\n"
"    padding-left: 20px;\n"
"}")
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 0, 0, 1, 1)
        self.password_label = QtWidgets.QLabel(self.form_grid)
        self.password_label.setStyleSheet("QLabel {\n"
"    Color: rgb(85, 85, 255);\n"
"    font: 63 12pt \"Lucida Sans\";\n"
"    padding-left: 20px;\n"
"}")
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)
        self.auth_btn = QtWidgets.QPushButton(self.form_grid)
        self.auth_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 255, 255);\n"
"    Color: rgb(85, 85, 255);\n"
"    font: 63 12pt \"Lucida Sans\";\n"
"    border: 1px solid grey;\n"
"    margin-left: 100px;\n"
"    margin-right: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.auth_btn.setObjectName("auth_btn")
        self.gridLayout.addWidget(self.auth_btn, 2, 0, 1, 2)
        IS_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(IS_main)
        QtCore.QMetaObject.connectSlotsByName(IS_main)

    def retranslateUi(self, IS_main):
        _translate = QtCore.QCoreApplication.translate
        IS_main.setWindowTitle(_translate("IS_main", "Информационная система \"Охранная служба\""))
        self.login_label.setText(_translate("IS_main", "Логин:"))
        self.password_label.setText(_translate("IS_main", "Пароль:"))
        self.auth_btn.setText(_translate("IS_main", "Войти"))
