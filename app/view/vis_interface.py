# coding:utf-8
'''
Created on 2024-12-2
三等分，从左到右：
左侧：总体分析
中间：上肢、中段、下肢波动图片
右侧：上肢、中段、下肢文字分析
'''
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import Qt, QEasingCurve, QUrl
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QLabel, QHBoxLayout, QFrame, QSizePolicy
from qfluentwidgets import (Pivot, qrouter, SegmentedWidget, TabBar, CheckBox, ComboBox,
                            TabCloseButtonDisplayMode, BodyLabel, SpinBox, BreadcrumbBar,
                            SegmentedToggleToolWidget, FluentIcon, PushButton, PrimaryPushButton)

from .gallery_interface import GalleryInterface, ToolBar
from ..common.translator import Translator
from ..common.style_sheet import StyleSheet
from ..components.sample_card import SampleCardView_small
from PyQt5.QtWidgets import  QVBoxLayout
import PyQt5.QtWebEngineWidgets
from ..UI.TOTAL_3 import CustomWidget
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtWidgets import QWidget
from ..UI.LA import LA
from ..UI.RA import RA
from ..UI.MP import MP
from ..UI.LL import LL
from ..UI.RL import RL

class VisInterface(GalleryInterface):
    """ Navigation view interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title="Analyze for YOU",
            subtitle="Make every piece of data meaningful",
            extrabutton= 1,
            parent=parent
        )
        self.setObjectName('visInterface')
        #self.pushButton = PushButton(self)
        self.pushButton = PushButton(FIF.FLAG,'your pose')
        #self.loadSamples()
        self.addExampleCard(
            title = self.tr('total'),
            widget = CustomWidget(self),
            #sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/navigation/segmented_widget/demo.py'
        )
        self.addExampleCard(
            title=self.tr('ARMs'),
            widget=Segmented_ArmInterface(self),
            #sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/navigation/segmented_widget/demo.py'
        )

        self.addExampleCard(
            title=self.tr('BODY&LEGs'),
            widget=Segmented_OtherInterface(self),
            #sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/navigation/segmented_widget/demo.py'
        )
    def createToggleToolWidget(self):
        w = SegmentedToggleToolWidget(self)
        w.addItem('k1', FluentIcon.TRANSPARENT)
        w.addItem('k2', FluentIcon.CHECKBOX)
        w.addItem('k3', FluentIcon.CONSTRACT)
        w.setCurrentItem('k1')
        return w

    def loadSamples(self):
        """ load samples """
        #Demo页面
        iconView = SampleCardView_small(self.view)
        iconView.addSampleCard_small(
            routeKey="viewInterface",
            index=0
        )
        self.vBoxLayout.addWidget(iconView)


class ArmInterface(QWidget):
    """ Pivot interface """
    Nav = Pivot
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(850,400)
        self.pivot = self.Nav(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)
        #引入子interface

        self.LAInterface = LA(self)
        self.RAInterface = RA(self)

        # add items to pivot
        self.addSubInterface(self.LAInterface, 'LA', self.tr('Left Arm'))
        self.addSubInterface(self.RAInterface, 'RA', self.tr('Right Arm'))
        #self.addSubInterface(self.SuggestInterface, 'S1', self.tr('Suggestions'))

        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignLeft)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        StyleSheet.NAVIGATION_VIEW_INTERFACE.apply(self)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.LAInterface)
        self.pivot.setCurrentItem(self.LAInterface.objectName())

        qrouter.setDefaultRouteKey(self.stackedWidget, self.LAInterface.objectName())

    def addSubInterface(self, widget: QWidget, objectName, text):
        widget.setObjectName(objectName)
        #widget.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def addSubInterface_html(self, html_content, objectName, text):
        # 创建 QWebEngineView 实例
        webview = PyQt5.QtWebEngineWidgets.QWebEngineView()
        webview.setObjectName(objectName)
        webview.setHtml(html_content)
        # 添加到堆叠窗口
        self.stackedWidget.addWidget(webview)

        # 假设的添加导航项（根据实际导航控件实现）
        # 这里需要根据你的 pivot 控件的具体实现来调整
        # 例如，如果 pivot 有一个 addItem 方法：
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(webview)
        )
        print(f"Added navigation item: {text} with objectName: {objectName}")
    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())
        qrouter.push(self.stackedWidget, widget.objectName())


class Segmented_ArmInterface(ArmInterface):

    Nav = SegmentedWidget

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout.removeWidget(self.pivot)
        self.vBoxLayout.insertWidget(0, self.pivot)


class OtherInterface(QWidget):
    """ Pivot interface """
    Nav = Pivot
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(850,400)
        self.pivot = self.Nav(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.LLInterface = LL(self)
        self.RLInterface = RL(self)
        self.MPInterface = MP(self)
        # add items to pivot
        self.addSubInterface(self.LLInterface, 'LL', self.tr('Left Leg'))
        self.addSubInterface(self.RLInterface, 'RL', self.tr('Right Leg'))
        self.addSubInterface(self.MPInterface, 'MP', self.tr('Middle Part'))

        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignLeft)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        StyleSheet.NAVIGATION_VIEW_INTERFACE.apply(self)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.LLInterface)
        self.pivot.setCurrentItem(self.LLInterface.objectName())

        qrouter.setDefaultRouteKey(self.stackedWidget, self.LLInterface.objectName())

    def addSubInterface(self, widget: QWidget, objectName, text):
        widget.setObjectName(objectName)
        # widget.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())
        qrouter.push(self.stackedWidget, widget.objectName())


class Segmented_OtherInterface(OtherInterface):

    Nav = SegmentedWidget

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout.removeWidget(self.pivot)
        self.vBoxLayout.insertWidget(0, self.pivot)