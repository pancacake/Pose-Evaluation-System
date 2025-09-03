# -*- coding: utf-8 -*-
import json
import os
#from typing import re
import re
import typing

# Form implementation modified to LA widget
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be maintained.

from PyQt5 import QtCore, QtGui, QtWidgets

import qfluentwidgets


class MP(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.txt_file_path = r"D:\PESUI\app\data\analyze.txt"
        self.extracted_contents = self.extract_la_contents()
        self.setupUi()


    def setupUi(self):
        self.setObjectName("LA")
        self.resize(821, 354)

        self.ProgressBar = ProgressBar(self)
        self.ProgressBar.setGeometry(QtCore.QRect(160, 20, 201, 4))
        self.ProgressBar.setValue(90)
        self.ProgressBar.setObjectName("ProgressBar")

        self.StrongBodyLabel = StrongBodyLabel(self)
        self.StrongBodyLabel.setGeometry(QtCore.QRect(80, 10, 111, 19))
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")

        self.BodyLabel = BodyLabel(self)
        self.BodyLabel.setGeometry(QtCore.QRect(80, 30, 63, 19))
        self.BodyLabel.setObjectName("BodyLabel")

        self.BodyLabel_2 = BodyLabel(self)
        self.BodyLabel_2.setGeometry(QtCore.QRect(80, 50, 63, 19))

        self.BodyLabel_2.setObjectName("BodyLabel_2")

        self.ProgressBar_2 = ProgressBar(self)
        self.ProgressBar_2.setGeometry(QtCore.QRect(160, 40, 171, 4))
        self.ProgressBar_2.setValue(87)
        self.ProgressBar_2.setObjectName("ProgressBar_2")

        self.ProgressBar_3 = ProgressBar(self)
        self.ProgressBar_3.setGeometry(QtCore.QRect(160, 60, 171, 4))
        self.ProgressBar_3.setValue(94)
        self.ProgressBar_3.setObjectName("ProgressBar_3")

        self.BodyLabel_3 = BodyLabel(self)
        self.BodyLabel_3.setGeometry(QtCore.QRect(620, 20, 181, 321))
        self.BodyLabel_3.setObjectName("BodyLabel_3")

        self.ImageLabel = ImageLabel(self)
        self.ImageLabel.setGeometry(QtCore.QRect(0, 0, 72, 72))
        self.ImageLabel.setObjectName("ImageLabel")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 80, 591, 261))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap(r"D:\pose-evaluation\HoT-main\demo\usr_vis\middle_body\standard_middle_body.jpg"))  # Replace with your image path
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); border-radius: 20px;")
        self.label.setScaledContents(True)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LA", "LA Widget"))
        self.StrongBodyLabel.setText(_translate("LA", "Total Score"))
        self.BodyLabel.setText(_translate("LA", "Body label"))
        self.BodyLabel_2.setText(_translate("LA", "Body label"))
        self.BodyLabel_3.setText(_translate("LA", f'{self.extracted_contents}'))
        # Removed text setting for the image label since it now contains an image
        # self.label.setText(_translate("LA", "TextLabel"))

    def extract_la_contents(self):
        """
        从指定文件中提取所有在 'LA:' 后且在分号 ';' 前的内容。

        参数:
            file_path (str): 文件的路径。

        返回:
            list: 包含所有提取内容的列表。
        """
        pattern = r'MP:(.*?);'
        extracted_contents = []

        with open(self.txt_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(pattern, content)
            extracted_contents = [match.strip() for match in matches]

        return extracted_contents[0]


from qfluentwidgets import BodyLabel, ImageLabel, ProgressBar, StrongBodyLabel
