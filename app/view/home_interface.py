# coding:utf-8
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QPainterPath, QLinearGradient
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from qfluentwidgets import ScrollArea, isDarkTheme, FluentIcon
from qfluentwidgets import FluentIcon as FIF
from ..common.config import cfg, HELP_URL, REPO_URL, EXAMPLE_URL, FEEDBACK_URL, QTFLUENT_URL, HOT_URL, release_url
from ..common.icon import Icon, FluentIconBase
from ..components.link_card import LinkCardView
from ..components.sample_card import SampleCardView
from ..common.style_sheet import StyleSheet

#更新导航内容
class BannerWidget(QWidget):
    """ Banner widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(500)

        self.vBoxLayout = QVBoxLayout(self)
        self.galleryLabel = QLabel('Welcome', self)
        self.banner = QPixmap(r"D:\PESUI\app\resource\images\10252nd.png")
        self.linkCardView = LinkCardView(self)

        self.galleryLabel.setObjectName('galleryLabel')

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.vBoxLayout.addWidget(self.galleryLabel)
        self.vBoxLayout.addWidget(self.linkCardView, 1, Qt.AlignBottom)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.linkCardView.addCard(
            r"D:\PESUI\app\resource\images\BJTU.png",
            self.tr('About us'),
            self.tr(
                'We are team from BJTU, China. This is a project work based on Chinese College Students Innovation Competition.'),
            release_url
        )

        self.linkCardView.addCard(
            FluentIcon.GITHUB,
            self.tr('About Model'),
            self.tr(
                'Find out the basic pose-recognition model on Github. We appreciate the contribution of the model Team.'),
            HOT_URL
        )

        self.linkCardView.addCard(
            ':/gallery/images/logo.png',
            self.tr('About UI'),
            self.tr('Visit the official website of UI library.'),
            QTFLUENT_URL
        )

        self.linkCardView.addCard(
            FluentIcon.FEEDBACK,
            self.tr('Contact us'),
            self.tr('Contact and help us to further imporve our system.'),
            FEEDBACK_URL
        )

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        w, h = self.width(), self.height()
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
        path = path.simplified()

        # init linear gradient effect
        gradient = QLinearGradient(0, 0, 0, h)

        # draw background color
        if not isDarkTheme():
            gradient.setColorAt(0, QColor(207, 216, 228, 255))
            gradient.setColorAt(1, QColor(207, 216, 228, 0))
        else:
            gradient.setColorAt(0, QColor(0, 0, 0, 255))
            gradient.setColorAt(1, QColor(0, 0, 0, 0))
            
        painter.fillPath(path, QBrush(gradient))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), transformMode=Qt.SmoothTransformation)
        painter.fillPath(path, QBrush(pixmap))


class HomeInterface(ScrollArea):
    """ Home interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = BannerWidget(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()

        self.loadSamples()

    def __initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('homeInterface')
        StyleSheet.HOME_INTERFACE.apply(self)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

    def loadSamples(self):
        """ load samples """
        #Demo页面
        iconView = SampleCardView(self.tr('Starts your DEMO'), self.view)
        iconView.addSampleCard(
            icon= FIF.PEOPLE,
            title="Demo",
            content=self.tr("Upload and evaluate your own pose."),
            routeKey="uploadInterface",
            index=0
        )
        self.vBoxLayout.addWidget(iconView)

        # navigation
        navigationView = SampleCardView(self.tr('See your POSE'), self.view)
        navigationView.addSampleCard(
            icon=FIF.TRANSPARENT,
            title="Total score",
            content=self.tr(
                "Shows the trail of navigation taken to the current location."),
            routeKey="visInterface",
            index=0
        )
        '''
        navigationView.addSampleCard(
            icon=":/gallery/images/controls/Pivot.png",
            title="Arms",
            content=self.tr(
                "Presents information from different sources in a tabbed view."),
            routeKey="navigationViewInterface",
            index=1
        )
        navigationView.addSampleCard(
            icon=":/gallery/images/controls/TabView.png",
            title="Legs and Middle parts",
            content=self.tr(
                "Presents information from different sources in a tabbed view."),
            routeKey="navigationViewInterface",
            index=2
        )
        '''
        self.vBoxLayout.addWidget(navigationView)

        # date time samples
        dateTimeView = SampleCardView(self.tr('AI for anything'), self.view)
        dateTimeView.addSampleCard(
            icon=FIF.HELP,
            title="AI chatting",
            content=self.tr("A control that lets a user pick a date value using a calendar."),
            routeKey="aiInterface",
            index=0
        )
        self.vBoxLayout.addWidget(dateTimeView)


        '''
        # view samples
        collectionView = SampleCardView(self.tr('Principles and Data'), self.view)
        collectionView.addSampleCard(
            icon=":/gallery/images/controls/ListView.png",
            title="ListView",
            content=self.tr(
                "A control that presents a collection of items in a vertical list."),
            routeKey="viewInterface",
            index=0
        )

        collectionView.addSampleCard(
            icon=":/gallery/images/controls/DataGrid.png",
            title="TableView",
            content=self.tr(
                "The DataGrid control provides a flexible way to display a collection of data in rows and columns."),
            routeKey="viewInterface",
            index=1
        )
        collectionView.addSampleCard(
            icon=":/gallery/images/controls/TreeView.png",
            title="TreeView",
            content=self.tr(
                "The TreeView control is a hierarchical list pattern with expanding and collapsing nodes that contain nested items."),
            routeKey="viewInterface",
            index=2
        )
        collectionView.addSampleCard(
            icon=":/gallery/images/controls/FlipView.png",
            title="FlipView",
            content=self.tr(
                "Presents a collection of items that the user can flip through,one item at a time."),
            routeKey="viewInterface",
            index=4
        )

        self.vBoxLayout.addWidget(collectionView)
        '''
