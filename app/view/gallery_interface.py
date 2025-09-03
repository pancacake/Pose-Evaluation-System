# coding:utf-8
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QEvent, QTimer
from PyQt5.QtGui import QDesktopServices, QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame

from qfluentwidgets import (ScrollArea, PushButton, ToolButton, FluentIcon,
                            isDarkTheme, IconWidget, Theme, ToolTipFilter, TitleLabel, CaptionLabel,
                            StrongBodyLabel, BodyLabel, toggleTheme, PrimaryPushButton, InfoBar, InfoBarIcon,
                            InfoBarPosition, ProgressRing, IndeterminateProgressRing)
from ..common.config import cfg, FEEDBACK_URL, HELP_URL, EXAMPLE_URL
from ..common.icon import Icon
from ..common.style_sheet import StyleSheet
from ..common.signal_bus import signalBus
from run_server import run_server
#ex card，去掉下面的链接
#把原来的那个版面改回去。

class SeparatorWidget(QWidget):
    """ Seperator widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(6, 16)

    def paintEvent(self, e):
        painter = QPainter(self)
        pen = QPen(1)
        pen.setCosmetic(True)
        c = QColor(255, 255, 255, 21) if isDarkTheme() else QColor(0, 0, 0, 15)
        pen.setColor(c)
        painter.setPen(pen)

        x = self.width() // 2
        painter.drawLine(x, 0, x, self.height())


class ToolBar(QWidget):
    """ Tool bar """
    extrastate = 0

    def __init__(self, title, subtitle, extrabutton,parent=None):
        super().__init__(parent=parent)
        self.titleLabel = TitleLabel(title, self)
        self.subtitleLabel = CaptionLabel(subtitle, self)

        self.documentButton = PushButton(
            self.tr('Documentation'), self, FluentIcon.DOCUMENT)
        self.sourceButton = PushButton(self.tr('Source'), self, FluentIcon.GITHUB)
        self.themeButton = ToolButton(FluentIcon.CONSTRACT, self)
        self.separator = SeparatorWidget(self)
        self.supportButton = ToolButton(FluentIcon.MESSAGE, self)
        self.feedbackButton = ToolButton(FluentIcon.FEEDBACK, self)
        if extrabutton == 1:
            self.exampleButton = PrimaryPushButton(self.tr('Example'), self, FluentIcon.CODE)

        if extrabutton == 2:
            self.runButton = PrimaryPushButton(self.tr('Run'), self, FluentIcon.PLAY)
            self.runButton.clicked.connect(self.run)

        if extrabutton == 3:
            self.downloadButton = PrimaryPushButton(self.tr('Download'), self, FluentIcon.DOWNLOAD)
            self.downloadButton.clicked.connect(self.download)

        self.vBoxLayout = QVBoxLayout(self)
        self.buttonLayout = QHBoxLayout()

        self.__initWidget(extrabutton)

    def __initWidget(self, extrabutton):
        self.setFixedHeight(138)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 12, 36, 4)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        self.vBoxLayout.addSpacing(0)
        self.vBoxLayout.addLayout(self.buttonLayout, 1)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

        self.buttonLayout.setSpacing(10)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self.buttonLayout.addWidget(self.documentButton, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.sourceButton, 0, Qt.AlignLeft)
        if extrabutton == 1:
            self.buttonLayout.addWidget(self.exampleButton, 0, Qt.AlignLeft)
        if extrabutton == 2:
            self.buttonLayout.addWidget(self.runButton, 0, Qt.AlignLeft)
        if extrabutton ==3:
            self.buttonLayout.addWidget(self.downloadButton, 0, Qt.AlignLeft)
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.themeButton, 0, Qt.AlignRight)
        self.buttonLayout.addWidget(self.separator, 0, Qt.AlignRight)
        self.buttonLayout.addWidget(self.supportButton, 0, Qt.AlignRight)
        self.buttonLayout.addWidget(self.feedbackButton, 0, Qt.AlignRight)

        self.themeButton.installEventFilter(ToolTipFilter(self.themeButton))
        self.supportButton.installEventFilter(ToolTipFilter(self.supportButton))
        self.feedbackButton.installEventFilter(
            ToolTipFilter(self.feedbackButton))
        self.themeButton.setToolTip(self.tr('Toggle theme'))
        self.supportButton.setToolTip(self.tr('Support me'))
        self.feedbackButton.setToolTip(self.tr('Send feedback'))

        self.themeButton.clicked.connect(lambda: toggleTheme(True))
        self.supportButton.clicked.connect(signalBus.supportSignal)
        self.documentButton.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(HELP_URL)))
        self.sourceButton.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(EXAMPLE_URL)))
        self.feedbackButton.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL)))

        self.subtitleLabel.setTextColor(QColor(96, 96, 96), QColor(216, 216, 216))

    def run(self):
        run_server()  # 调用从其他文件导入的函数
        # 创建并显示自建库的消息窗口
        InfoBar.success(
            title="开始运行",
            content="正在进行模型上传及评估，请稍候...",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=5000,
            parent=self
        )
    def download(self):
        InfoBar.success(
            title="开始下载",
            content="正在下载本次评估数据，请稍候...",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=5000,
            parent=self
        )


class ExampleCard(QWidget):
    """ Example card """

    #def __init__(self, title, widget: QWidget, sourcePath, stretch=0, parent=None):
    def __init__(self, title, widget: QWidget, stretch=0, parent=None):
        super().__init__(parent=parent)
        self.widget = widget
        self.stretch = stretch

        self.titleLabel = StrongBodyLabel(title, self)
        self.card = QFrame(self)

        self.sourceWidget = QFrame(self.card)
        #self.sourcePath = sourcePath
        #self.sourcePathLabel = BodyLabel(
        #    self.tr('Source code'), self.sourceWidget)
        #self.linkIcon = IconWidget(FluentIcon.LINK, self.sourceWidget)

        self.vBoxLayout = QVBoxLayout(self)
        self.cardLayout = QVBoxLayout(self.card)
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout(self.sourceWidget)

        self.__initWidget()
        self.__initLayout()


    def __initWidget(self):
        #self.linkIcon.setFixedSize(16, 16)
        self.__initLayout()

        #self.sourceWidget.setCursor(Qt.PointingHandCursor)
        #self.sourceWidget.installEventFilter(self)

        self.card.setObjectName('card')
        #self.sourceWidget.setObjectName('sourceWidget')


    def __initLayout(self):
        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
        self.cardLayout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
        self.topLayout.setSizeConstraint(QHBoxLayout.SetMinimumSize)

        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setContentsMargins(12, 12, 12, 12)
        self.bottomLayout.setContentsMargins(18, 18, 18, 6)
        self.cardLayout.setContentsMargins(0, 0, 0, 0)

        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.card, 0, Qt.AlignTop)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

        self.cardLayout.setSpacing(0)
        self.cardLayout.setAlignment(Qt.AlignTop)
        self.cardLayout.addLayout(self.topLayout, 0)
        self.cardLayout.addWidget(self.sourceWidget, 0, Qt.AlignBottom)

        self.widget.setParent(self.card)
        self.topLayout.addWidget(self.widget)
        if self.stretch == 0:
            self.topLayout.addStretch(1)

        self.widget.show()

        #self.bottomLayout.addWidget(self.sourcePathLabel, 0, Qt.AlignLeft)
        #self.bottomLayout.addStretch(1)
        #self.bottomLayout.addWidget(self.linkIcon, 0, Qt.AlignRight)
        self.bottomLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def eventFilter(self, obj, e):
        if obj is self.sourceWidget:
            if e.type() == QEvent.MouseButtonRelease:
                QDesktopServices.openUrl(QUrl(self.sourcePath))

        return super().eventFilter(obj, e)


class GalleryInterface(ScrollArea):
    """ Gallery interface """

    def __init__(self, title: str, subtitle: str, extrabutton, parent=None):
        """
        Parameters
        ----------
        title: str
            The title of gallery

        subtitle: str
            The subtitle of gallery

        parent: QWidget
            parent widget
        """
        super().__init__(parent=parent)
        self.view = QWidget(self)
        self.toolBar = ToolBar(title, subtitle, extrabutton,self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, self.toolBar.height(), 0, 0)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setContentsMargins(36, 10,36 ,10)  #调整页边距

        self.view.setObjectName('view')
        StyleSheet.GALLERY_INTERFACE.apply(self)

    #def addExampleCard(self, title, widget, sourcePath: str, stretch=0):
    def addExampleCard(self, title, widget, stretch=0):
        card = ExampleCard(title, widget,stretch, self.view)
        self.vBoxLayout.addWidget(card, 0, Qt.AlignTop)
        return card

    def scrollToCard(self, index: int):
        """ scroll to example card """
        w = self.vBoxLayout.itemAt(index).widget()
        self.verticalScrollBar().setValue(w.y())

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.toolBar.resize(self.width(), self.toolBar.height())
