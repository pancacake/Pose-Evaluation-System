from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget
#from PyQt6 import QtCore, QtWidgets
from qfluentwidgets import BodyLabel, ImageLabel, PixmapLabel, ProgressBar, StrongBodyLabel
from qfluentwidgets.multimedia import VideoWidget

#调整各模块位置，加入一个overall评估的位置
class TOTAL(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(1800, 608)

        self.demo = VideoWidget(parent = self)
        self.demo.setGeometry(QtCore.QRect(10, 110, 691, 411))
        self.demo.setVideo(QUrl.fromLocalFile("D:\pose-evaluation\HoT-main\demo\output\standard\standard.mp4"))
        self.demo.setObjectName("demo")

        self.body = ImageLabel(self)
        self.body.setGeometry(QtCore.QRect(750, 50, 381, 491))
        self.body.setBorderRadius(8,8,8,8)
        self.body.setObjectName("bodypic")

        self.ProgressBar = ProgressBar(parent=self)
        self.ProgressBar.setGeometry(QtCore.QRect(230, 20, 132, 4))
        self.ProgressBar.setObjectName("ProgressBar")

        self.StrongBodyLabel_2 = StrongBodyLabel(parent=self)
        self.StrongBodyLabel_2.setGeometry(QtCore.QRect(100, 10, 111, 19))
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")

        self.BodyLabel = BodyLabel(parent=self)
        self.BodyLabel.setGeometry(QtCore.QRect(100, 40, 63, 19))
        self.BodyLabel.setObjectName("BodyLabel")

        self.BodyLabel_2 = BodyLabel(parent=self)
        self.BodyLabel_2.setGeometry(QtCore.QRect(100, 70, 63, 19))
        self.BodyLabel_2.setObjectName("BodyLabel_2")

        self.ProgressBar_2 = ProgressBar(parent=self)
        self.ProgressBar_2.setGeometry(QtCore.QRect(190, 50, 132, 4))
        self.ProgressBar_2.setObjectName("ProgressBar_2")

        self.ProgressBar_3 = ProgressBar(parent=self)
        self.ProgressBar_3.setGeometry(QtCore.QRect(190, 80, 132, 4))
        self.ProgressBar_3.setObjectName("ProgressBar_3")

        self.ImageLabel = ImageLabel(parent=self)
        self.ImageLabel.setGeometry(QtCore.QRect(10, 10, 72, 72))
        self.ImageLabel.setBorderRadius(8,8,8,8)
        self.ImageLabel.setObjectName("ImageLabel")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.StrongBodyLabel_2.setText(_translate("Form", "Strong body label2"))
        self.BodyLabel.setText(_translate("Form", "Body label"))
        self.BodyLabel_2.setText(_translate("Form", "Body label"))
