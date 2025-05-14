from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout,
                             QTextBrowser, QSizePolicy)
from PyQt5.QtGui import QPixmap, QBitmap, QPainter, QColor, QPainterPath, QFontMetrics
from PyQt5.QtCore import Qt, QSize, QFile
import sys


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
        h = self.text_frame.document().size().height()
        w = self.text_frame.document().size().width()
        self.resize(300, 250)

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
        if self.adjusting:
            return
        self.adjusting = True
        super().resizeEvent(event)
        h = self.text_frame.document().size().height()
        w = self.text_frame.document().size().width()
        self.setFixedHeight(h+65)
        self.adjusting = False


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.my_list = QListWidget()
        self.my_list.setStyleSheet("QListWidget { background-color: transparent; }")
        self.my_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.my_list.setUniformItemSizes(False)
        ll = QVBoxLayout()
        ll.addWidget(self.my_list)
        self.setLayout(ll)


if __name__ == 'main__':
    app = QApplication(sys.argv)
    a = ChatBubble(text="她常安静地坐在图书馆角落，阳光透过玻璃洒在身上，给清瘦的轮廓镀上一层柔和的金边。微风轻拂，垂落的发丝轻轻扫过白净的侧脸，"
                        "眉眼低垂，眼睫在眼眶下投出淡淡的阴影，似是带着几分不食人间烟火的疏离感。下课铃响，人群涌动，她抱着书本慢慢踱出教室，步履轻缓，"
                        "不疾不徐，像是怕惊扰了周遭的宁静。浅浅的酒窝在嘴角若隐若现，笑容藏着几分羞涩，眼神清澈又温柔，仿若静谧湖水，波澜不兴，只在偶尔抬头时，"
                        "才让人心神一颤，沉醉其中。", avatar_file='img.png', client_name='Lucia', is_send=True)
    b = ChatBubble(text="外你", avatar_file='img.png', client_name='Lucia', is_send=False)
    b.show()
    sys.exit(app.exec_())


from PyQt5.QtWidgets import QFrame, QLabel, QWidget, QVBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import QPoint, Qt


class QFrameBubble(QFrame):
    def __init__(self, text='', parent=None):
        super().__init__(parent)
        self.pen = "#000000"  # 画笔颜色
        self.brush = "#E0F7FA"  # 笔刷颜色
        self.triangle_position = 'left'  # 三角形位置
        # 创建 QLabel 显示文字
        self.label = QLabel(text, self)
        self.label.setStyleSheet("background: transparent;")  # 设置背景透明
        self.label.setWordWrap(True)  # 如果文字过长，自动换行

        # 设置布局，将 QLabel 添加到 QFrameBubble 中
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.setContentsMargins(20, 10, 20, 10)  # 设置气泡内部边距
        self.setLayout(layout)
        # 设置无边框，以便自定义绘制
        self.setFrameStyle(QFrame.NoFrame)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # 设置画笔和笔刷
        pen = QPen(QColor(self.pen))
        painter.setPen(pen)
        brush = QBrush(QColor(self.brush))
        painter.setBrush(brush)

        # 绘制气泡的矩形部分
        rect = self.rect()
        rect.adjust(10, 10, -10, -10)  # 调整矩形的大小
        painter.drawRoundedRect(rect, 10, 10)

        if self.triangle_position == 'left':
            # 绘制气泡的三角部分在左侧中央
            points = [
                QPoint(rect.left(), rect.center().y() + 10),
                QPoint(rect.left() - 10, rect.center().y()),
                QPoint(rect.left(), rect.center().y() - 10)
            ]
        else:
            # 绘制气泡的三角部分在右侧中央
            points = [
                QPoint(rect.right(), rect.center().y() - 10),
                QPoint(rect.right() + 10, rect.center().y()),
                QPoint(rect.right(), rect.center().y() + 10)
            ]
        painter.drawPolygon(*points)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 200)

        # 创建自定义气泡
        bubble1 = QFrameBubble("聊天气泡,三角形在左侧", parent=self)

        bubble2 = QFrameBubble(parent=self)
        bubble2.pen = "#E0F7FA"
        bubble2.brush = "#E0F7FA"
        bubble2.triangle_position = 'right'
        bubble2.label.setText('聊天气泡,三角形在右侧')
        bubble2.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(bubble1)
        layout.addWidget(bubble2)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Example()
    window.show()
    app.exec_()
