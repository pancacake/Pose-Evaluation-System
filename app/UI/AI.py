# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import AvatarWidget

class AIWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AIWidget, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AIWidget")
        self.resize(538, 622)

        # 创建布局
        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.mainLayout.setContentsMargins(20, 10, 20, 10)
        self.mainLayout.setSpacing(10)

        # AvatarWidget
        self.avatarWidget = AvatarWidget(self)
        self.avatarWidget.setFixedSize(96, 96)
        self.avatarWidget.setObjectName("avatarWidget")
        self.mainLayout.addWidget(self.avatarWidget, alignment=QtCore.Qt.AlignTop)

        # QTextBrowser
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setMinimumSize(381, 621)
        self.mainLayout.addWidget(self.textBrowser)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AIWidget", "AI Widget"))