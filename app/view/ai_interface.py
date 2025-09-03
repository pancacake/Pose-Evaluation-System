from PyQt5.QtCore import Qt, pyqtSlot, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QApplication
from qfluentwidgets import (
    SearchLineEdit, HeaderCardWidget, BodyLabel, IconWidget,
    InfoBarIcon, HyperlinkLabel, PlainTextEdit
)
from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..view.llm_worker import LLMWorker  # 导入新建的 LLMWorker 类

class AIInput(HeaderCardWidget):
    """ AI 输入卡片 """
    questionSubmitted = pyqtSignal(str)  # 定义信号，传递字符串类型的问题

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('Feel Free to Ask')
        self.infoLabel = BodyLabel('Qwen2.5:3b', self)
        self.successIcon = IconWidget(InfoBarIcon.SUCCESS, self)

        self.vBoxLayout = QVBoxLayout()
        self.hBoxLayout = QHBoxLayout()

        self.successIcon.setFixedSize(16, 16)
        self.hBoxLayout.setSpacing(10)
        self.vBoxLayout.setSpacing(16)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.hBoxLayout.addWidget(self.successIcon)
        self.hBoxLayout.addWidget(self.infoLabel)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        #self.vBoxLayout.addWidget(self.detailButton)

        self.lineEdit = SearchLineEdit(self)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setFixedWidth(500)
        self.lineEdit.setFixedHeight(40)

        # 连接搜索信号到槽函数
        self.lineEdit.searchSignal.connect(self.on_search)

        self.lineLayout = QVBoxLayout()
        self.lineLayout.addWidget(self.lineEdit)

        self.viewLayout.addLayout(self.vBoxLayout)
        self.viewLayout.addLayout(self.lineLayout)

    @pyqtSlot(str)
    def on_search(self, text: str):
        """ 处理搜索信号 """
        self.questionSubmitted.emit(text)


class AIInfo(HeaderCardWidget):
    """ AI 信息展示卡片 """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('AI Responses')
        #self.infoLabel = BodyLabel('AI 模型已连接', self)
        #self.successIcon = IconWidget(InfoBarIcon.SUCCESS, self)
        #self.detailButton = HyperlinkLabel('详情', self)

        self.vBoxLayout = QVBoxLayout()
        self.hBoxLayout = QHBoxLayout()

        #self.successIcon.setFixedSize(16, 16)
        self.hBoxLayout.setSpacing(10)
        self.vBoxLayout.setSpacing(16)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)

        #self.hBoxLayout.addWidget(self.successIcon)
        #self.hBoxLayout.addWidget(self.infoLabel)
        self.vBoxLayout.addLayout(self.hBoxLayout)

        self.textEdit = PlainTextEdit(self)
        self.textEdit.setPlainText("")
        self.textEdit.setReadOnly(True)
        self.textEdit.setFixedWidth(850)
        self.textEdit.setFixedHeight(400)

        self.textLayout = QVBoxLayout()
        self.textLayout.addWidget(self.textEdit)

        self.viewLayout.addLayout(self.vBoxLayout)
        self.viewLayout.addLayout(self.textLayout)

    def display_answer(self, answer: str):
        self.textEdit.setPlainText(answer)


class AiInterface(GalleryInterface):
    """ AI 接口 """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title="AI for anything",
            subtitle='Ask and improve your pose',
            extrabutton=0,
            parent=parent
        )
        self.setObjectName('aiInterface')
        self.aiinfo = AIInfo()
        self.aiinput = AIInput()
        self.addExampleCard(
            title=self.tr('Supported by Qwen2.5:3b'),
            widget=self.createHorizontalGroupCards(),
        )

        # 初始化线程和工作器
        self.thread = QThread()
        self.worker = LLMWorker()
        self.worker.moveToThread(self.thread)

        # 连接信号
        self.aiinput.questionSubmitted.connect(self.handle_question)
        self.worker.responseReady.connect(self.aiinfo.display_answer)
        self.worker.errorOccurred.connect(self.display_error)

        # 启动线程
        self.thread.start()

    def createHorizontalGroupCards(self):
        """ 创建包含两个水平排列的卡片的容器 """
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(13)

        self.aiinput.setMinimumWidth(800)
        self.aiinfo.setMinimumWidth(800)

        layout.addWidget(self.aiinput)
        layout.addWidget(self.aiinfo)

        return container

    @pyqtSlot(str)
    def handle_question(self, question: str):
        """ 处理用户输入的问题并调用 LLMWorker """
        self.aiinfo.display_answer("Generating...")
        self.worker.set_prompt(question)

    @pyqtSlot(str)
    def display_error(self, error: str):
        """ 显示错误信息 """
        self.aiinfo.display_answer(f"调用模型时出错: {error}")
