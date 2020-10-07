from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommentWindow(object):
    def setupUi(self, CommentWindow):
        CommentWindow.setObjectName("CommentWindow")
        CommentWindow.resize(390, 304)
        CommentWindow.setStyleSheet("background-color: rgb(255, 252, 155);\n"
"border: 1px solid blue;\n"
"font: 63 12pt Lucida Sans;\n"
"color: rgb(85, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(CommentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comment = QtWidgets.QTextEdit(self.centralwidget)
        self.comment.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.comment.setObjectName("comment")
        self.gridLayout.addWidget(self.comment, 1, 1, 1, 1)
        self.ID_label = QtWidgets.QLabel(self.centralwidget)
        self.ID_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.ID_label.setObjectName("ID_label")
        self.gridLayout.addWidget(self.ID_label, 0, 0, 1, 1)
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 1, 1, 1)
        self.comment_label = QtWidgets.QLabel(self.centralwidget)
        self.comment_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.comment_label.setObjectName("comment_label")
        self.gridLayout.addWidget(self.comment_label, 1, 0, 1, 1)
        self.send_comment = QtWidgets.QPushButton(self.centralwidget)
        self.send_comment.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin: 20px;")
        self.send_comment.setObjectName("send_comment")
        self.gridLayout.addWidget(self.send_comment, 2, 0, 1, 2)
        CommentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CommentWindow)
        QtCore.QMetaObject.connectSlotsByName(CommentWindow)

    def retranslateUi(self, CommentWindow):
        _translate = QtCore.QCoreApplication.translate
        CommentWindow.setWindowTitle(_translate("CommentWindow", "Окно комментария"))
        self.ID_label.setText(_translate("CommentWindow", "ID заказа"))
        self.comment_label.setText(_translate("CommentWindow", "Комментарий"))
        self.send_comment.setText(_translate("CommentWindow", "Отправить"))