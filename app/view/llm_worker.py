from PyQt5.QtCore import QObject, pyqtSignal
from ollama import chat

class LLMWorker(QObject):
    """ 用于调用 Ollama 模型的工作线程 """
    responseReady = pyqtSignal(str)  # 用于发送生成的回答（现在发送的是格式化后的 history）
    errorOccurred = pyqtSignal(str)  # 用于发送错误信息

    def __init__(self):
        super().__init__()
        self.base_prompt = "你将扮演一名动作评价专家，根据我的动作得分、动作特点和你的总体分析，紧密围绕我的问题，向我提出改善建议。"
        self.question = ""
        self.history = []  # 用于存储对话历史

    def set_prompt(self, question: str):
        """ 设置用户问题，并启动模型调用 """
        self.question = question
        self.run_model()

    def run_model(self):
        """ 调用 Ollama 模型生成回答 """
        try:
            # 将用户的问题添加到 history 中
            self.history.append({"role": "user", "content": self.question})

            # 拼接消息，包括 base_prompt 和历史记录
            messages = [{"role": "system", "content": self.base_prompt}] + self.history

            # 调用 Ollama 模型（流式输出）
            answer = ""
            for chunk in chat(
                    model="qwen2.5:3b",  # 替换为实际模型名称
                    messages=messages,
                    stream=False
            ):
                # 检查 chunk 的内容
                if isinstance(chunk, tuple):
                    # 处理元组类型的 chunk
                    key, value = chunk
                    if key == "message" and hasattr(value, "content"):
                        # 提取 Message 对象中的 content 属性
                        content = value.content
                        if isinstance(content, str):
                            answer += content
                    else:
                        print(f"Received metadata: {key} = {value}")
                else:
                    # 处理其他未知格式
                    print(f"Unexpected chunk format: {chunk}")

            # 将模型的回答添加到 history 中
            self.history.append({"role": "assistant", "content": answer})

            # 格式化 history 为字符串形式
            formatted_history = self.format_history()

            # 发送格式化后的历史记录到显示区
            self.responseReady.emit(formatted_history)

        except Exception as e:
            self.errorOccurred.emit(f"模型调用出错: {str(e)}")

    def format_history(self) -> str:
        """ 格式化 history 数组为字符串形式，便于显示 """
        formatted = ""
        for entry in self.history:
            if entry["role"] == "user":
                formatted += f"You: {entry['content']}\n"
            elif entry["role"] == "assistant":
                formatted += f"Pose Assistant: {entry['content']}\n"
        return formatted