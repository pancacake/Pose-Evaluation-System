from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy  
from qfluentwidgets import BodyLabel, ImageLabel, ProgressBar, StrongBodyLabel  
from qfluentwidgets.multimedia import VideoWidget  

class CustomWidget(QWidget):  
    def __init__(self, parent=None):  
        super(CustomWidget, self).__init__(parent)  
        self.setupUi()  

    def setupUi(self):  
        self.setObjectName("CustomWidget")  
        self.setMinimumSize(1188,648)  # Set a reasonable minimum size

        # Main layout  
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)


        # Top Section Layout  
        #top_layout = QHBoxLayout()

        # Left Side Widgets
        bar1_layout = QHBoxLayout()
        bar2_layout = QHBoxLayout()
        bar3_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        leftall_layout = QVBoxLayout()
        left_layout.setSpacing(1)
        bar1_layout.setSpacing(5)
        bar2_layout.setSpacing(5)
        bar3_layout.setSpacing(5)
        main_layout.setSpacing(10)

        self.SubtitleLabel = StrongBodyLabel(self)
        self.SubtitleLabel.setText("Total Score")

        bar1_layout.addWidget(self.SubtitleLabel)

        self.BodyLabel = BodyLabel(self)  
        self.BodyLabel.setText("Body label")  
        bar2_layout.addWidget(self.BodyLabel)

        self.BodyLabel_2 = BodyLabel(self)  
        self.BodyLabel_2.setText("Body label")  
        bar3_layout.addWidget(self.BodyLabel_2)

        self.ProgressBar = ProgressBar(self)  
        self.ProgressBar.setValue(93)  # Example value
        self.ProgressBar.setCustomBarColor(QColor(255, 0, 0), QColor(255, 0, 0))
        bar1_layout.addWidget(self.ProgressBar)


        self.ProgressBar_2 = ProgressBar(self)
        self.ProgressBar_2.setValue(95)  # Example value
        bar2_layout.addWidget(self.ProgressBar_2)

        self.ProgressBar_3 = ProgressBar(self)  
        self.ProgressBar_3.setValue(89)  # Example value
        bar3_layout.addWidget(self.ProgressBar_3)
        left_layout.addLayout(bar1_layout)
        left_layout.addLayout(bar2_layout)
        left_layout.addLayout(bar3_layout)
        leftall_layout.addLayout(left_layout)
        # Image Labels  
        #images_layout = QHBoxLayout()
        #left_layout.addLayout(images_layout)

        self.ImageLabel = ImageLabel(r"D:\pose-evaluation\HoT-main\demo\usr_vis\colored_human_skeleton.jpg")
        #self.ImageLabel.setFixedSize(300,700)
        self.ImageLabel.scaledToHeight(500)
        self.ImageLabel.setBorderRadius(6,6,6,6)
        leftall_layout.addWidget(self.ImageLabel)

        #main_layout.addLayout(leftall_layout, stretch=1)
        main_layout.addLayout(leftall_layout)


        # Right Side Widgets (Videos)  
        videos_layout = QVBoxLayout()

        self.user = VideoWidget(parent=self)  
        self.user.setVideo(QUrl.fromLocalFile(r"C:\Users\赵\桌面\test3\standard_videos\demo\demotest1.mp4"))
        self.user.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  
        videos_layout.addWidget(self.user)  

        self.std = VideoWidget(parent=self)  
        self.std.setVideo(QUrl.fromLocalFile(r"D:\pose-evaluation\HoT-main\demo\output\user2\standard.mp4"))
        self.std.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  
        videos_layout.addWidget(self.std)  
        main_layout.addLayout(videos_layout, stretch=1)
        # Additional Widgets or Layouts can be added here  

    def retranslateUi(self):  
        _translate = QtCore.QCoreApplication.translate  
        self.setWindowTitle(_translate("CustomWidget", "Custom Widget"))
