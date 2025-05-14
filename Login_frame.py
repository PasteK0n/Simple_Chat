import json
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
import Login_frame_ui
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class LoginFrame(QWidget, Login_frame_ui.Ui_Form):
    Login_in_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(QWidget,self).__init__(parent)
        self.setupUi(self)
        self.set_ui()
        self.file_name = ''
        self.client_table = {}
        self.load_table()
        self.button_connect()

    def button_connect(self):
        self.Login_in_signal.connect(self.Login_in)
        self.Login_choice_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.Register_choice_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.Password_forget_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.Register_button.clicked.connect(self.register_new)
        self.stackedWidget.currentChanged.connect(self.text_clear)
        self.Login_button.clicked.connect(self.login_client)

    def set_ui(self):
        self.image_label.setStyleSheet("QLabel{border-image:url(./Local_source/Client_source/image/login_default.png);}")
        self.image_label.clear()

    def register_new(self):
        if len(self.Client_input_2.text()) < 6:
            QMessageBox.warning(self, '警告', '账号长度不能少于6位', QMessageBox.Yes, QMessageBox.Yes)
            return
        if not self.Email_input_2.text().endswith('.com'):
            QMessageBox.warning(self, '警告', '请输入正确的邮箱地址', QMessageBox.Yes, QMessageBox.Yes)
            return
        if len(self.Password_input_2.text()) < 6:
            QMessageBox.warning(self, '警告', '密码长度不能少于6位', QMessageBox.Yes, QMessageBox.Yes)
            return
        if self.Password_input_2.text() != self.Passwordd_input_confirm_2.text():
            QMessageBox.warning(self, '警告', '输入的两次密码不一致', QMessageBox.Yes, QMessageBox.Yes)
            return
        # TODO 验证码功能
        client = self.Client_input_2.text()
        password = self.Passwordd_input_confirm_2.text()
        client_email = self.Email_input_2.text()
        for i in list(self.client_table.items()):
            if i[0] == client_email:
                QMessageBox.warning(self, '警告', '该邮箱已经注册过！', QMessageBox.Yes, QMessageBox.Yes)
                return
            if i[1][0] == client:
                QMessageBox.warning(self, '警告', '该账号已存在', QMessageBox.Yes, QMessageBox.Yes)
                return
        QMessageBox.information(self, '通知', '注册成功！', QMessageBox.Yes, QMessageBox.Yes)
        self.save_new_client(client_email= client_email, client=client, password=password)
        if self.checkBox_3.checkState():
            self.Login_in_signal.emit(True)

    def login_client(self):
        if len(self.Client_input.text()) < 6:
            QMessageBox.warning(self, '警告', '账号长度不能少于6位', QMessageBox.Yes, QMessageBox.Yes)
            return
        if self.Client_password_input.text() == '':
            QMessageBox.warning(self, '警告', '密码不能为空', QMessageBox.Yes, QMessageBox.Yes)
            return
        for i in list(self.client_table.items()):
            if self.Client_input.text() == i[0] or self.Client_input.text() == i[1][0]:
                if self.Client_password_input.text() == i[1][1]:
                    self.Login_in_signal.emit(True)
                    return
        QMessageBox.warning(self, '警告', '该账号不存在或密码输入错误', QMessageBox.Yes, QMessageBox.Yes)

    def save_new_client(self, client_email, client, password):
        self.client_table[client_email] = (client, password)

    def closeEvent(self, a0):
        with open('Local_source\\Client_table\\Client_tabel.json', 'w', encoding='utf-8') as f:
            tmp = json.dumps(self.client_table, indent=3)
            f.write(tmp)
        a0.accept()

    def load_table(self):
        with open('Local_source\\Client_table\\Client_tabel.json', 'r', encoding='utf-8') as f:
            self.client_table = json.load(f)

    def text_clear(self):
        self.Client_input.clear()
        self.Client_password_input.clear()

        self.Client_input_2.clear()
        self.Email_input_2.clear()
        self.Password_input_2.clear()
        self.Passwordd_input_confirm_2.clear()
        self.Yanzhengma_input.clear()

        self.Email_input_3.clear()
        self.New_password_input.clear()
        self.Password_cofrim_input_3.clear()
        self.lineEdit_9.clear()

    def Login_in(self, state: bool):
        print('登入成功！')
        pass


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = LoginFrame()
    b.show()
    sys.exit(a.exec_())
