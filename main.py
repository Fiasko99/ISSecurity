import sys
import requests as r
import IS
import Profile
import Send_Order
import Comment
import Security
import datetime as dt
from dateutil import relativedelta
from PyQt5 import QtWidgets


def date_format(date):
    date = date.split(".")
    date = dt.date(int(date[2]),
                   int(date[1]),
                   int(date[0]))

    return date


def count_months(first_date, second_date):
    first_date = date_format(first_date)
    second_date = date_format(second_date)

    date = relativedelta.relativedelta(first_date, second_date)

    month = date.months if date.months > 0 else 1
    years = date.years if date.years > 0 else -1
    months = month * years * 12 if years > 0 else month

    return months


def mod_days(date):
    date = date_format(date)
    dt_now = dt.date.today()

    return date - dt_now


class ISMainWindow(QtWidgets.QMainWindow, IS.Ui_IS_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = -1
        self.auth_btn.clicked.connect(self.login_process)

    def login_process(self):
        login = self.login_line.text()
        password = self.password_line.text()

        security = r.get('http://localhost:3000/security').json()
        workers = security
        success = False
        for worker in security:
            if login == worker['username'] and password == worker['password']:
                success = True
                security = worker
            elif login == "admin" and password == "admin":
                self.window = SendOrderWindow()
                self.window.send_security(workers)
                self.window.show()
                self.close()
            elif login == "comment" and password == "comment":
                self.window = CommentWindow()
                self.window.show()
                self.close()
            elif login == "security" and password == "security":
                self.window = SecurityWindow()
                self.window.show()
                self.close()

        if success:
            order = r.get('http://localhost:3000/order').json()
            place = r.get('http://localhost:3000/place').json()
            output = r.get('http://localhost:3000/output').json()
            comment = r.get('http://localhost:3000/comment').json()

            for elem in order:
                if elem['id_security'] == security['id']:
                    order = elem
                else:
                    order = {
                        "id_security": security['id'],
                        "id_place": -1,
                        "id_output": -1,
                        "id_comment": -1,
                        "total_in_month": "-",
                        "id": -1
                    }

            for elem in place:
                if elem['id'] == order['id_place']:
                    place = elem
                else:
                    place = {
                        "id": -1,
                        "address": "-",
                        "note": "-"
                    }

            for elem in output:
                if elem['id'] == order['id_output']:
                    output = elem
                else:
                    output = {
                        "id": 1,
                        "data_rel": "-",
                        "data_exp": "-"
                    }

            for elem in comment:
                if elem['id'] == order['id_comment']:
                    comment = elem
                else:
                    comment = {
                        "id": -1,
                        "comment": "-"
                    }

            bd_worker = [security, place, output, comment, order]

            self.window = ProfileWindow(bd_worker)
            self.window.fill_labels()
            self.window.show()
            self.close()
        else:
            self.login_line.setText('Неверно введенны данные профиля')


class ProfileWindow(QtWidgets.QMainWindow, Profile.Ui_ProfileWindow):
    def __init__(self, data_base):
        super().__init__()
        self.setupUi(self)
        self.window = -1
        self.data_base = data_base
        self.logout_btn.clicked.connect(self.logout_process)

    def fill_labels(self):
        id_order = "Нет заказа"
        if self.data_base[4]['id'] != -1:
            id_order = self.data_base[4]['id']
        self.id_order.setText(str(id_order))

        name = self.data_base[0]['username']
        surname = self.data_base[0]['surname']
        name_surname = name + " " + surname
        self.name_surname.setText(name_surname)

        address = self.data_base[1]['address']
        note = self.data_base[1]['note']
        self.adress.setText(address + "\n" + note)

        date_rel = self.data_base[2]['data_rel']
        date_exp = self.data_base[2]['data_exp']
        left_d = ""
        if date_exp != "-":
            left_d = str(mod_days(date_exp)).split()[0]
        dates = date_rel + "\n" + date_exp
        self.dates.setText(dates + "\nДней осталось: " + left_d)

        comment = self.data_base[3]['comment']
        self.comment.setText(comment)

        pay = self.data_base[4]['total_in_month']
        s = ""
        if pay != "-":
            months = count_months(date_exp, date_rel)
            s = str(pay * months)
        self.sum_payment.setText(str(pay) + "\nИтого:" + s)

    def logout_process(self):
        self.window = ISMainWindow()
        self.window.show()
        self.close()


class SendOrderWindow(QtWidgets.QMainWindow, Send_Order.Ui_Send_OrderWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = -1
        self.send_btn.clicked.connect(self.send_process)

    def send_process(self):
        all_security = r.get('http://localhost:3000/security').json()
        worker = self.sort_security.currentText().split(" ")
        for security in all_security:
            if worker[0] == security['username']:
                id_worker = security['id']

                place = {
                    "address": self.address.text(),
                    "note": self.note.toPlainText()
                }

                url_place = 'http://localhost:3000/place'

                place_id = r.post(url_place, json=place).json()

                comment = {
                    "comment": ""
                }

                url_com = 'http://localhost:3000/comment'

                comment_id = r.post(url_com, json=comment).json()

                output = {
                    "data_rel": self.date_rel.text(),
                    "data_exp": self.date_exp.text()
                }

                url_out = 'http://localhost:3000/output'

                output_id = r.post(url_out, json=output).json()

                order = {
                    "id_security": id_worker,
                    "id_place": place_id['id'],
                    "id_output": comment_id['id'],
                    "id_comment": output_id['id'],
                    "total_in_month": self.pay_month.text()
                }

                r.post('http://localhost:3000/order', json=order)

                self.window = ISMainWindow()
                self.window.show()
                self.close()

    def send_security(self, workers):
        self.sort_security.clear()
        full_name = ["Выбрать"]
        for worker in workers:
            full_name.append(worker['username'] + " " + worker['surname'])

        self.sort_security.addItems(full_name)


class CommentWindow(QtWidgets.QMainWindow, Comment.Ui_CommentWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = -1
        self.send_comment.clicked.connect(self.send_and_close)

    def send_and_close(self):
        orders = r.get('http://localhost:3000/order').json()
        id_order = self.id.text()

        for order in orders:
            if order['id'] == int(id_order):
                id_comment = order['id_comment']

                comment = {
                    "comment": self.comment.toPlainText()
                }

                url_com = 'http://localhost:3000/comment/'

                r.put(url_com + str(id_comment), json=comment)

                self.window = ISMainWindow()
                self.window.show()
                self.close()


class SecurityWindow(QtWidgets.QMainWindow, Security.Ui_SecurityWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = -1
        self.save_btn.clicked.connect(self.save_process)

    def save_process(self):

        arr_sec = self.login_input.text().split(" ")

        name = arr_sec[0]
        surname = arr_sec[1]
        password = self.password_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()

        security = {
            "username": name,
            "surname": surname,
            "password": password,
            "email": email,
            "phone": phone
        }

        url_sec = 'http://localhost:3000/security'

        r.post(url_sec, json=security)

        self.window = ISMainWindow()
        self.window.show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ISMainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
