# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1182, 831)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(31, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tool_ = QtWidgets.QWidget(self.frame)
        self.tool_.setMinimumSize(QtCore.QSize(55, 0))
        self.tool_.setMaximumSize(QtCore.QSize(55, 16777215))
        self.tool_.setStyleSheet("#tool_{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.467662 rgba(240, 209, 240, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"")
        self.tool_.setObjectName("tool_")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tool_)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_4 = QtWidgets.QFrame(self.tool_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_4.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setStyleSheet("border-image: url(:/chat_icon/chat_icon/1559839459357.jpeg);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12.addWidget(self.frame_4)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.tool_)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setStyleSheet("QPushButton\n"
"{border-image: url(:/chat_icon/chat_icon/qipao_empty.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        background-size: 100% 100%;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;}\n"
"QPushButton:hover{\n"
"    border-image: url(:/chat_icon/chat_icon/qipao_fill.png);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tool_)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(:/chat_icon/chat_icon/icons8-customer-50.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;}\n"
"QPushButton:hover{\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-customer-fill-50 .png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(17, 438, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tool_)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-image: url(:/chat_icon/chat_icon/set_empty.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;}\n"
"QPushButton:hover{\n"
"    border-image: url(:/chat_icon/chat_icon/set_fill.png);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_10.addWidget(self.tool_)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setStyleSheet("background-color: rgb(255, 228, 255);\n"
"color: rgb(255, 228, 255);\n"
"border:None")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(25, 25))
        self.frame_3.setMaximumSize(QtCore.QSize(25, 25))
        self.frame_3.setStyleSheet("border-image: url(:/chat_icon/chat_icon/serash.png)0 0 0 0;\n"
"background-color: transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(127, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(:/chat_icon/chat_icon/add_icon.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 25px;\n"
"        min-height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-add-p-50.png);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setStyleSheet("background-color: rgb(255, 228, 255);\n"
"color: rgb(255, 228, 255);\n"
"border:None")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:None")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setStyleSheet("background-color: rgb(255, 228, 255);\n"
"color: rgb(255, 228, 255);\n"
"border:None")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_10.addWidget(self.line_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setStyleSheet("background-color: rgb(255, 228, 255);\n"
"color: rgb(255, 228, 255);\n"
"border:None")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(27, 27))
        self.pushButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border-image: url(:/chat_icon/chat_icon/icons8-减法-30.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 27px;\n"
"        min-height: 27px;}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-减法-p-30.png);\n"
"background-color: rgb(0, 0, 0); \n"
"}\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(27, 27))
        self.pushButton_13.setMaximumSize(QtCore.QSize(27, 27))
        self.pushButton_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet("QPushButton\n"
"{border-image: url(:/chat_icon/chat_icon/icons8-full-screen-50.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 27px;\n"
"        min-height: 27px;}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-full-screen-p-50.png);\n"
"background-color: rgb(0, 0, 0); \n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_6.addWidget(self.pushButton_13)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(27, 27))
        self.pushButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(:/chat_icon/chat_icon/icons8-乘-30.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 27px;\n"
"        min-height: 27px;}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-乘-p-30.png);\n"
"background-color: rgb(0, 0, 0); \n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(7, -1, 7, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: transparent;")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("border-image: url(:/chat_icon/qianjin);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setStyleSheet("background-color: rgb(255, 228, 255);\n"
"color: rgb(255, 228, 255);\n"
"border:None")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 776, 382))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setStyleSheet("background-color: rgb(255, 228, 255);\n"
"color: rgb(255, 228, 255);\n"
"border:None")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border-image: url(:/chat_icon/chat_icon/icons8-快乐-30.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-快乐-p-30.png);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_8.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_9.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border-image: url(:/chat_icon/chat_icon/icons8-folder-50.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-folder-p-50.png);\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_8.addWidget(self.pushButton_9)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_11.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"border-image: url(:/chat_icon/chat_icon/icons8-chat-bubble-50.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/chat_icon/chat_icon/icons8-chat-bubble-p-50.png);\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_8.addWidget(self.pushButton_11)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_10.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("QPushButton{border-image: url(:/chat_icon/chat_icon/icons8-video-call-50.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"        background-position: center;\n"
"        border: none;\n"
"        min-width: 30px;\n"
"        min-height: 30px;}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 240, 240,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    border-image: url(:/chat_icon/chat_icon/icons8-video-call-p-50.png);\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_8.addWidget(self.pushButton_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setBaseSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border:None\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.send_button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setMinimumSize(QtCore.QSize(70, 50))
        self.send_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("QPushButton\n"
"{color: rgb(0,0, 0);\n"
"background-color: rgb(242, 231, 255);\n"
"border-radius: 20px;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(242, 231, 255,0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 0, 0); \n"
"color:rgb(255,228,255)\n"
"}\n"
"")
        self.send_button.setObjectName("send_button")
        self.horizontalLayout_9.addWidget(self.send_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.setStretch(4, 5)
        self.verticalLayout_3.setStretch(7, 2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setStyleSheet("background-color: rgb(255, 228, 255);\n"
"color: rgb(255, 228, 255);\n"
"border:None")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_10.addWidget(self.line_10)
        self.horizontalLayout_10.setStretch(1, 3)
        self.horizontalLayout_10.setStretch(3, 8)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "群聊对象名字"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.send_button.setText(_translate("Form", "发送"))
import chart_frame_icon_rc
