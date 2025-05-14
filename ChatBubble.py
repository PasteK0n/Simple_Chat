import logging

from PyQt5 import sip
from PyQt5.QtCore import Qt, QTimer, QSize, pyqtSignal, QFile
from PyQt5.QtWidgets import (QWidget, QLabel, QTextBrowser, QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QScrollArea, QApplication, QMainWindow)
from PyQt5.QtGui import QPixmap, QFontMetrics, QTextDocument
import weakref
import chat_text


class ChatBubble(QWidget):
    def __init__(self, text: str, avatar_file: str, client_name: str, is_send: bool):
        super().__init__()
        self.avatar_file = avatar_file
        self.text_data = text
        self.client_name = client_name
        self.text_frame = QTextBrowser()
        self.avatar_image = QPixmap()
        self.avatar_label = QLabel()
        self.name_label = QLabel()
        self.adjusting = False
        if is_send:
            self.init_ui_send()
        else:
            self.init_ui_no_send()

    def setup_avatar(self):
        if QFile.exists(self.avatar_file):
            self.avatar_image.load(self.avatar_file)
            self.avatar_label.setPixmap(self.avatar_image.scaled(50, 50, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
            self.avatar_label.setStyleSheet("""border:None;border-radius:25px;""")
        else:
            self.avatar_image.load("Local_source\\Client_source\\image\\default.jpg")
            self.avatar_label.setPixmap(self.avatar_image.scaled(50, 50, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
            self.avatar_label.setStyleSheet("""border:None;border-radius:25px;""")

    def setup_name(self):
        self.name_label.setText(self.client_name)
        self.setStyleSheet("""QLabel{family-font:'微软雅黑';
                                font-size:20px;
                                font-weight:bold;
                                color:rgb(0,0,0)};
                                QWidget{background: transparent;}""")

    def adjust_text_size(self):
        self.setMaximumWidth(850)
        self.setMinimumWidth(350)
        self.text_frame.setMaximumWidth(850)
        self.text_frame.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_frame.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.text_frame.show()
        tmp = QTextDocument()
        tmp.setPlainText(self.text_data)
        tmp.setTextWidth(400)
        self.setFixedHeight(tmp.size().height()+65)

    def load_text(self):
        self.text_frame.document().setPlainText(self.text_data)
        self.text_frame.setStyleSheet("""QTextBrowser{border-radius:10px;
                                            font-family:'微软雅黑';
                                            font-size:17px;
                                            padding:7px;
                                            background-color:rgb(255,228,255)}""")
        self.adjust_text_size()

    def init_ui_no_send(self):
        self.setup_name()
        self.load_text()
        self.setup_avatar()
        layout1 = QVBoxLayout()
        layout1.addWidget(self.avatar_label)
        layout1.addStretch()
        layout2 = QVBoxLayout()
        layout2.addWidget(self.name_label)
        layout_text = QHBoxLayout()
        blank = QLabel()
        layout_text.addWidget(self.text_frame, 5)
        layout_text.addWidget(blank, 3)
        layout2.addLayout(layout_text)
        main_layout = QHBoxLayout()
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        self.setLayout(main_layout)

    def init_ui_send(self):
        self.setup_name()
        self.load_text()
        self.setup_avatar()
        layout1 = QVBoxLayout()
        layout1.addWidget(self.avatar_label)
        layout1.addStretch()
        layout2 = QVBoxLayout()
        layout2.addWidget(self.name_label, alignment=Qt.AlignRight)
        layout_text = QHBoxLayout()
        blank = QLabel()
        layout_text.addWidget(blank, 3)
        layout_text.addWidget(self.text_frame, 5)
        layout2.addLayout(layout_text)
        main_layout = QHBoxLayout()
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout1)
        self.setLayout(main_layout)

    def resizeEvent(self, event):
        if self.adjusting or self.text_frame.document().size().height() == 0:
            return
        self.adjusting = True
        super().resizeEvent(event)
        h = self.text_frame.document().size().height()
        self.setFixedHeight(h+65)
        self.adjusting = False
