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
class UploadInterface(GalleryInterface):
    """ Icon interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title="YOUR Pose",
            subtitle="visualize yourself",
            extrabutton= 2,
            parent=parent
        )
        self.setObjectName('uploadInterface')
        #布局
        '''''
        self.addExampleCard(
            title=self.tr('Upload Video'),
            widget=ActionSettingsCard(self),
            #sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/navigation/segmented_widget/demo.py'
        )

        #standard pose
        self.addExampleCard(
            title=self.tr('Your Pose'),
            widget=self.createVideoPlayerCard(),
            #sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/navigation/segmented_widget/demo.py'
        )
        '''''

        self.addExampleCard(
            title=self.tr('UPLOAD your Pose'),
            widget=self.createHorizontalGroupCards(),
        )

    def createHorizontalGroupCards(self):
        """ 创建包含两个水平排列的GroupHeaderCard的容器 """
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(13)

        # 创建第一个GroupHeaderCard
        actionSettingsCard = ActionSettingsCard(self)
        actionSettingsCard.setMinimumWidth(645)

        # 创建第二个GroupHeaderCard
        loadvideocard = loadvideoCard(self)
        loadvideocard.setMinimumWidth(645)

        # 将两个卡片添加到水平布局中
        layout.addWidget(actionSettingsCard)
        layout.addWidget(loadvideocard)

        return container

class ActionSettingsCard(GroupHeaderCardWidget):

    def __init__(self, parent=None, scroll_widget=None, home_interface=None):
        super().__init__(parent)
        self.home_interface = home_interface
        self.scrollWidget = scroll_widget  # 将 scroll_widget 赋值给实例属性
        self.setTitle("上传视频")
        self.setBorderRadius(8)
        self.setMinimumWidth(400)  # 设置最小宽度为400，可以根据需要调整

        self.comboBox = ComboBox()
        self.comboBox.setFixedWidth(260)
        self.comboBox.addItems(["test1", "test2"])
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)  # 连接信号

        # 定义动作类型对应的视频路径
        self.video_paths = {
            "test1": r"D:\PESUI\standard_videos\test1.mp4",
            "test2": r"D:\PESUI\standard_videos\test2.mp4"
        }

        self.bottomLayout = QHBoxLayout()

        self.bottomLayout.setSpacing(8)
        self.bottomLayout.setContentsMargins(24, 15, 24, 20)

        self.bottomLayout.addStretch(1)
        self.bottomLayout.setAlignment(Qt.AlignVCenter)

        group = self.addGroup(FIF.SPEED_HIGH, "选择动作类型", "选择你要进行评估的动作", self.comboBox)
        group.setSeparatorVisible(True)

        # 添加视频播放器
        self.videoPlayerCard = self.createVideoPlayerCard()
        self.vBoxLayout.addWidget(self.videoPlayerCard)
        self.vBoxLayout.addLayout(self.bottomLayout)

    def createVideoPlayerCard(self):
        """ 创建视频播放器卡片 """
        videoCard = QWidget()  # 创建一个新的 QWidget 作为卡片
        layout = QVBoxLayout(videoCard)  # 设置布局

        # 设置布局的边距和间距
        layout.setContentsMargins(10, 10, 10, 10)  # 设置边距
        layout.setSpacing(5)  # 设置间距

        # 创建视频播放器
        self.videoWidget = VideoWidget(videoCard)
        default_video = self.video_paths[self.comboBox.currentText()]
        self.videoWidget.setVideo(QUrl.fromLocalFile(default_video))  # 设置默认视频文件路径
        self.videoWidget.play()  # 播放视频
        self.videoWidget.setFixedSize(650, 395)  # 设置固定大小（可选）

        # 将视频播放器添加到布局中
        layout.addWidget(self.videoWidget)

        return videoCard  # 返回包含视频播放器的卡片

    def on_combobox_changed(self, index):
        """ 当 ComboBox 选择改变时，加载对应的视频 """
        selected_option = self.comboBox.currentText()
        video_path = self.video_paths.get(selected_option, "")
        if video_path:
            self.videoWidget.setVideo(QUrl.fromLocalFile(video_path))
            self.videoWidget.play()


class loadvideoCard(GroupHeaderCardWidget):

    def __init__(self, parent=None, scroll_widget=None, home_interface=None):
        super().__init__(parent)
        self.home_interface = home_interface
        self.scrollWidget = scroll_widget  # 将 scroll_widget 赋值给实例属性
        self.setTitle("上传视频")
        self.setBorderRadius(8)
        self.setMinimumWidth(400)  # 设置最小宽度为400，可以根据需要调整

        # 初始化UI组件
        self.hintIcon = IconWidget(FIF.INFO)
        self.hintLabel = BodyLabel("选择你的输入方式👉")
        self.recordButton = PrimaryPushButton(FIF.PLAY_SOLID, "录制")
        self.uploadButton = PushButton(FIF.VIEW, "上传")
        self.bottomLayout = QHBoxLayout()

        self.hintIcon.setFixedSize(16, 16)
        self.bottomLayout.setSpacing(8)
        self.bottomLayout.setContentsMargins(24, 15, 24, 20)

        self.bottomLayout.addWidget(self.hintIcon, 0, Qt.AlignLeft)
        self.bottomLayout.addWidget(self.hintLabel, 0, Qt.AlignLeft)
        self.bottomLayout.addStretch(1)
        self.bottomLayout.addWidget(self.uploadButton, 0, Qt.AlignRight)
        self.bottomLayout.addWidget(self.recordButton, 0, Qt.AlignRight)
        self.bottomLayout.setAlignment(Qt.AlignVCenter)

        # 添加视频播放器
        self.vBoxLayout.addLayout(self.bottomLayout)
        self.videoPlayerCard = self.createVideoPlayerCard()
        self.vBoxLayout.addWidget(self.videoPlayerCard)

        # 连接按钮的点击事件到对应的槽函数
        self.uploadButton.clicked.connect(self.upload_video)
        self.recordButton.clicked.connect(self.open_record_dialog)

    def createVideoPlayerCard(self):
        """ 创建视频播放器卡片 """
        videoCard = QWidget()  # 创建一个新的 QWidget 作为卡片
        layout = QVBoxLayout(videoCard)  # 设置布局

        # 设置布局的边距和间距
        layout.setContentsMargins(10, 10, 10, 10)  # 设置边距
        layout.setSpacing(5)  # 设置间距

        # 创建视频播放器
        self.videoWidget = VideoWidget(videoCard)
        # 初始化时不加载任何视频
        self.videoWidget.setFixedSize(630, 395)  # 设置固定大小（可选）

        # 将视频播放器添加到布局中
        layout.addWidget(self.videoWidget)

        return videoCard  # 返回包含视频播放器的卡片

    def upload_video(self):
        """ 处理上传视频的逻辑 """
        options = QFileDialog.Options()
        # 仅允许选择视频文件，可以根据需要调整过滤器
        file_filter = "Video Files (*.mp4 *.avi *.mov *.mkv);;All Files (*)"
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频文件",
            "",
            file_filter,
            options=options
        )
        if file_path:
            # 此处可以添加将文件路径传回系统或进行其他处理的代码
            # 例如：
            # self.home_interface.handle_uploaded_file(file_path)
            print(f"用户上传的文件路径: {file_path}")  # 或者其他处理逻辑

            # 设置视频播放器播放上传的视频
            self.videoWidget.setVideo(QUrl.fromLocalFile(file_path))
            self.videoWidget.play()

            # 创建并显示自建库的消息窗口
            w = InfoBar.new(
                icon=FluentIcon.FLAG,
                title='上传成功',
                content=f"成功上传文件: {file_path}",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=2000,
                parent=self
            )
            w.setCustomBackgroundColor('white', '#202020')
        else:
            # 用户未选择文件时，停止视频播放并清空视频源
            self.videoWidget.pause()
            self.videoWidget.setVideo(QUrl())  # 清空视频源
            print("用户未上传任何视频文件。")

    def open_record_dialog(self):
        """ 打开视频录制对话框 """
        if self.record_dialog is None or not self.record_dialog.isVisible():
            self.record_dialog = VideoRecordDialog()
            self.record_dialog.show()
        else:
            self.record_dialog.raise_()
            self.record_dialog.activateWindow()

class VideoRecordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        try:
            self.setWindowTitle("视频录制")
            self.setGeometry(150, 150, 800, 600)
            self.setModal(False)  # 设置为非模态窗口
            self.setWindowFlags(self.windowFlags() | Qt.Window)  # 确保作为独立窗口

            self.layout = QVBoxLayout()
            self.setLayout(self.layout)

            # 检查是否有可用的摄像头
            available_cameras = QCameraInfo.availableCameras()
            if not available_cameras:
                QMessageBox.critical(self, "错误", "未检测到摄像头设备。")
                self.close()
                return

            # 使用第一个可用的摄像头
            self.camera = QCamera(available_cameras[0])
            self.viewfinder = QCameraViewfinder()
            self.camera.setViewfinder(self.viewfinder)
            self.layout.addWidget(self.viewfinder)

            # 控制按钮布局
            self.button_layout = QHBoxLayout()
            self.layout.addLayout(self.button_layout)

            self.start_button = QPushButton("开始录制")
            self.stop_button = QPushButton("停止录制")
            self.close_button = QPushButton("关闭窗口")

            self.button_layout.addWidget(self.start_button)
            self.button_layout.addWidget(self.stop_button)
            self.button_layout.addWidget(self.close_button)

            # 设置按钮的初始状态
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

            # 连接按钮的点击事件到槽函数
            self.start_button.clicked.connect(self.start_recording)
            self.stop_button.clicked.connect(self.stop_recording)
            self.close_button.clicked.connect(self.close_dialog)

            # 设置视频录制器
            self.media_recorder = QMediaRecorder(self.camera)
            # 设置输出文件
            save_directory = os.path.join(os.getcwd(), "recorded_videos")
            os.makedirs(save_directory, exist_ok=True)
            self.output_file = os.path.join(save_directory, "output_" + self.get_timestamp() + ".mp4")
            self.media_recorder.setOutputLocation(QUrl.fromLocalFile(self.output_file))
            self.media_recorder.setContainerFormat("mp4")

            # 启动摄像头
            self.camera.start()

        except Exception as e:
            QMessageBox.critical(self, "错误", f"初始化录制窗口时发生错误:\n{e}")
            self.close()

    def get_timestamp(self):
        """ 获取当前时间戳，用于生成唯一的文件名 """
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @pyqtSlot()
    def start_recording(self):
        """ 开始录制视频 """
        if self.media_recorder.state() == QMediaRecorder.StoppedState:
            self.media_recorder.record()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            QMessageBox.information(self, "录制开始", "视频录制已开始。")

    @pyqtSlot()
    def stop_recording(self):
        """ 停止录制视频 """
        if self.media_recorder.state() == QMediaRecorder.RecordingState:
            self.media_recorder.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            QMessageBox.information(self, "录制结束", f"视频已保存到:\n{self.output_file}")

    @pyqtSlot()
    def close_dialog(self):
        """ 关闭录制窗口 """
        if self.media_recorder.state() == QMediaRecorder.RecordingState:
            reply = QMessageBox.question(
                self,
                "确认",
                "录制仍在进行中，是否确定关闭？",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.No:
                return
            else:
                self.media_recorder.stop()
        self.camera.stop()
        self.close()

    def closeEvent(self, event):
        """ 确保在窗口关闭时释放摄像头和录制器资源 """
        if self.media_recorder.state() == QMediaRecorder.RecordingState:
            self.media_recorder.stop()
        self.camera.stop()
        event.accept()