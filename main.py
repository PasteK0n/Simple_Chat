import sys

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
import chat_frame_ui
import ChatBubble
import Login_frame


class chat_frame(QWidget, chat_frame_ui.Ui_Form):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.msg_now = ''
        self.setupUi(self)
        self.set_ui()
        self.Button_connect()
        self.scrollArea_Widget = QWidget()
        self.scrollArea_layout = QVBoxLayout()
        self.scrollArea_Widget.setLayout(self.scrollArea_layout)
        self.scrollArea.setWidget(self.scrollArea_Widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea_layout.addStretch()

    def set_ui(self):
        self.setMinimumWidth(700)
        self.setMinimumHeight(500)

    def Button_connect(self):
        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        self.msg_now = self.textEdit.toPlainText()
        if self.msg_now == '':
            return
        tmp = ChatBubble.ChatBubble(text=self.msg_now, avatar_file='1111', client_name='Lucia', is_send=True)
        self.scrollArea_layout.addWidget(tmp)
        self.scrollArea_Widget.update()
        self.scrollArea.update()
        self.textEdit.clear()


class ChatMain:
    def __init__(self):
        self.login_frame = Login_frame.LoginFrame()
        self.chat_frame = chat_frame()
        self.login_frame.show()
        self.login_frame.Login_in_signal.connect(self.handle_signal)

    def handle_signal(self, state):
        self.chat_frame.show()
        self.login_frame.close()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = ChatMain()
    sys.exit(a.exec_())
