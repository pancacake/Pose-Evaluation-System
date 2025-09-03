# coding:utf-8
import os
from typing import List
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, pyqtSlot
from PyQt5.QtMultimedia import QCameraInfo, QCamera, QMediaRecorder
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QPushButton, QFileDialog, \
    QMessageBox, QDialog
from qfluentwidgets import (FluentIcon, IconWidget, FlowLayout, isDarkTheme,
                            Theme, applyThemeColor, SmoothScrollArea, SearchLineEdit, StrongBodyLabel,
                            BodyLabel, GroupHeaderCardWidget, ComboBox, InfoBarIcon, PrimaryPushButton, PushButton,
                            ExpandGroupSettingCard, InfoBar, InfoBarPosition)
from qfluentwidgets.multimedia import VideoWidget

from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from qfluentwidgets import FluentIcon as FIF

#把选择和输入都放到同一个界面里
class ViewInterface(GalleryInterface):
    """ Icon interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title="Help & Developer",
            subtitle="Get the raw data and explore more",
            extrabutton= 3,
            parent=parent
        )
        self.helpWidget = HelpWidget(self)
        self.setObjectName('viewInterface')
        self.addExampleCard(
            title=self.tr('Add standard videos'),
            widget=self.helpWidget,
        )


from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import PushButton


class HelpWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("HelpWidget")
        self.setFixedSize(1070, 650)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 1060, 640))
        self.label.setObjectName("label")
        # 加载图片并设置到QLabel中
        pixmap = QtGui.QPixmap(r"D:\PESUI\app\resource\images\viewer_end.png")  # 替换为你的图片路径
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)  # 使图片自适应QLabel的大小


        self.pushButton = PushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(70, 70, 151, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = PushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 170, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("HelpWidget", "Form"))
        #self.label.setText(_translate("HelpWidget", "TextLabel"))
        self.pushButton.setText(_translate("HelpWidget", "Push button"))
        self.pushButton_2.setText(_translate("HelpWidget", "Push button"))
