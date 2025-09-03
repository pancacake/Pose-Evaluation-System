from PyQt5.QtCore import Qt, QRectF, QUrl, QRect
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QPainterPath, QLinearGradient
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from qfluentwidgets import BodyLabel, ImageLabel, PixmapLabel, ProgressBar, StrongBodyLabel
from qfluentwidgets.multimedia import VideoWidget


class VisualizationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("VisualizationWidget")
        self.resize(1000,850)
        self.setupUi()

    def setupUi(self):
        # Create layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Top section with labels and progress bars
        top_layout = QHBoxLayout()

        # Image Labels
        image_layout = QVBoxLayout()
        self.image_label = ImageLabel(self)
        self.image_label.setFixedSize(72, 72)
        image_layout.addWidget(self.image_label)

        self.image_label_2 = ImageLabel(self)
        self.image_label_2.setFixedSize(72, 72)
        image_layout.addWidget(self.image_label_2)

        top_layout.addLayout(image_layout)

        # Labels and Progress Bars
        labels_layout = QVBoxLayout()

        self.strong_body_label = StrongBodyLabel(self)
        self.strong_body_label.setText("Strong body label")
        labels_layout.addWidget(self.strong_body_label)

        self.body_label = BodyLabel(self)
        self.body_label.setText("Body label")
        labels_layout.addWidget(self.body_label)

        self.body_label_2 = BodyLabel(self)
        self.body_label_2.setText("Body label")
        labels_layout.addWidget(self.body_label_2)

        top_layout.addLayout(labels_layout)

        progress_layout = QVBoxLayout()
        self.progress_bar = ProgressBar(self)
        self.progress_bar.setFixedHeight(4)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(50)
        progress_layout.addWidget(self.progress_bar)

        self.progress_bar_2 = ProgressBar(self)
        self.progress_bar_2.setFixedHeight(4)
        progress_layout.addWidget(self.progress_bar_2)

        self.progress_bar_3 = ProgressBar(self)
        self.progress_bar_3.setFixedHeight(4)
        progress_layout.addWidget(self.progress_bar_3)

        top_layout.addLayout(progress_layout)

        main_layout.addLayout(top_layout)

        # Video part
        self.user = VideoWidget(parent=self)
        self.user.setGeometry(QRect(400, 10, 471, 261))
        self.user.setVideo(QUrl.fromLocalFile(r"D:\pose-evaluation\HoT-main\demo\output\standard\standard.mp4"))
        self.user.setObjectName("user")
        self.std = VideoWidget(parent=self)
        self.std.setGeometry(QRect(400, 290, 471, 261))
        self.std.setVideo(QUrl.fromLocalFile(r"D:\pose-evaluation\HoT-main\demo\output\standard\standard.mp4"))
        self.std.setObjectName("std")

        videomap_layout = QVBoxLayout()
        videomap_layout.addWidget(self.user)
        videomap_layout.addWidget(self.std)
        main_layout.addLayout(videomap_layout)

        self.setLayout(main_layout)

    def retranslateUi(self):
        self.setWindowTitle("Visualization Widget")
        self.strong_body_label.setText("Strong body label")
        self.body_label.setText("Body label")
        self.body_label_2.setText("Body label")
