from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        ProfileWindow.setObjectName("ProfileWindow")
        ProfileWindow.resize(800, 600)
        ProfileWindow.setMinimumSize(QtCore.QSize(800, 600))
        ProfileWindow.setMaximumSize(QtCore.QSize(800, 600))
        ProfileWindow.setStyleSheet("background-color: rgb(255, 255, 200);\n"
"font: 63 12pt Lucida Sans;\n"
"color: rgb(85, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(ProfileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.form_profile = QtWidgets.QWidget(self.centralwidget)
        self.form_profile.setGeometry(QtCore.QRect(60, 50, 681, 501))
        self.form_profile.setStyleSheet("border: 1px solid blue;")
        self.form_profile.setObjectName("form_profile")
        self.gridLayout = QtWidgets.QGridLayout(self.form_profile)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.adress = QtWidgets.QLabel(self.form_profile)
        self.adress.setStyleSheet("margin-right: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.adress.setObjectName("adress")
        self.gridLayout.addWidget(self.adress, 6, 1, 1, 1)
        self.dates = QtWidgets.QLabel(self.form_profile)
        self.dates.setStyleSheet("margin-right: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.dates.setObjectName("dates")
        self.gridLayout.addWidget(self.dates, 7, 1, 1, 1)
        self.payment_label = QtWidgets.QLabel(self.form_profile)
        self.payment_label.setStyleSheet("margin-left: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.payment_label.setObjectName("payment_label")
        self.gridLayout.addWidget(self.payment_label, 9, 0, 1, 1)
        self.id_order = QtWidgets.QLabel(self.form_profile)
        self.id_order.setStyleSheet("margin-right: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.id_order.setObjectName("id_order")
        self.gridLayout.addWidget(self.id_order, 4, 1, 1, 1)
        self.order_label = QtWidgets.QLabel(self.form_profile)
        self.order_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin-left: 5px;")
        self.order_label.setObjectName("order_label")
        self.gridLayout.addWidget(self.order_label, 4, 0, 1, 1)
        self.sum_payment = QtWidgets.QLabel(self.form_profile)
        self.sum_payment.setStyleSheet("margin-right: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.sum_payment.setObjectName("sum_payment")
        self.gridLayout.addWidget(self.sum_payment, 9, 1, 1, 1)
        self.title_label = QtWidgets.QLabel(self.form_profile)
        self.title_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin: 10px;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 3, 0, 1, 2)
        self.name_surname_label = QtWidgets.QLabel(self.form_profile)
        self.name_surname_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin-left: 5px;")
        self.name_surname_label.setObjectName("name_surname_label")
        self.gridLayout.addWidget(self.name_surname_label, 5, 0, 1, 1)
        self.date_label = QtWidgets.QLabel(self.form_profile)
        self.date_label.setStyleSheet("margin-left: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.date_label.setObjectName("date_label")
        self.gridLayout.addWidget(self.date_label, 7, 0, 1, 1)
        self.comment = QtWidgets.QLabel(self.form_profile)
        self.comment.setStyleSheet("margin-right: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.comment.setObjectName("comment")
        self.gridLayout.addWidget(self.comment, 8, 1, 1, 1)
        self.name_surname = QtWidgets.QLabel(self.form_profile)
        self.name_surname.setStyleSheet("margin-right: 5px;\n"
"background-color: rgb(170, 255, 255);")
        self.name_surname.setObjectName("name_surname")
        self.gridLayout.addWidget(self.name_surname, 5, 1, 1, 1)
        self.adress_label = QtWidgets.QLabel(self.form_profile)
        self.adress_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin-left: 5px;")
        self.adress_label.setObjectName("adress_label")
        self.gridLayout.addWidget(self.adress_label, 6, 0, 1, 1)
        self.comment_label = QtWidgets.QLabel(self.form_profile)
        self.comment_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin-left: 5px;")
        self.comment_label.setObjectName("comment_label")
        self.gridLayout.addWidget(self.comment_label, 8, 0, 1, 1)
        self.logout_btn = QtWidgets.QPushButton(self.form_profile)
        self.logout_btn.setStyleSheet("margin: 10px;\n"
"background-color: rgb(170, 255, 255);")
        self.logout_btn.setObjectName("logout_btn")
        self.gridLayout.addWidget(self.logout_btn, 10, 0, 1, 2)
        ProfileWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileWindow)

    def retranslateUi(self, ProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileWindow.setWindowTitle(_translate("ProfileWindow", "Профиль"))
        self.adress.setText(_translate("ProfileWindow", "TextLabel"))
        self.dates.setText(_translate("ProfileWindow", "TextLabel"))
        self.payment_label.setText(_translate("ProfileWindow", "Месячная выплата"))
        self.id_order.setText(_translate("ProfileWindow", "TextLabel"))
        self.order_label.setText(_translate("ProfileWindow", "Заказ"))
        self.sum_payment.setText(_translate("ProfileWindow", "TextLabel"))
        self.title_label.setText(_translate("ProfileWindow", "Текущий заказ"))
        self.name_surname_label.setText(_translate("ProfileWindow", "Инициалы"))
        self.date_label.setText(_translate("ProfileWindow", "Даты"))
        self.comment.setText(_translate("ProfileWindow", "TextLabel"))
        self.name_surname.setText(_translate("ProfileWindow", "TextLabel"))
        self.adress_label.setText(_translate("ProfileWindow", "Адрес"))
        self.comment_label.setText(_translate("ProfileWindow", "Отзыв"))
        self.logout_btn.setText(_translate("ProfileWindow", "Выйти из профиля"))
