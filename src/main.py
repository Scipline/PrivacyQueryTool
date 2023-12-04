import sys
import base64
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QStyleFactory
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import QThread, Signal
import requests
import json
import pyperclip

class QueryThread(QThread):
    result_signal = Signal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url).text
        self.result_signal.emit(response)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("隐私查询软件")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.qq_group = QGroupBox("QQ查绑")
        self.qq_layout = QFormLayout(self.qq_group)
        self.qq_input = QLineEdit()
        self.qq_query_button = QPushButton("查询QQ号码")
        self.qq_result = QLabel()
        self.qq_layout.addRow(QLabel("请输入要查询的QQ:"), self.qq_input)
        self.qq_layout.addRow(self.qq_query_button)
        self.qq_layout.addRow(self.qq_result)

        self.phone_group = QGroupBox("手机号反查")
        self.phone_layout = QFormLayout(self.phone_group)
        self.phone_input = QLineEdit()
        self.phone_query_button = QPushButton("查询手机号")
        self.phone_result = QLabel()
        self.phone_layout.addRow(QLabel("请输入手机号:"), self.phone_input)
        self.phone_layout.addRow(self.phone_query_button)
        self.phone_layout.addRow(self.phone_result)

        self.weibo_group = QGroupBox("微博查绑")
        self.weibo_layout = QFormLayout(self.weibo_group)
        self.weibo_input = QLineEdit()
        self.weibo_button = QPushButton("查询微博ID")
        self.weibo_result = QLabel()
        self.weibo_layout.addRow(QLabel("请输入微博ID"), self.weibo_input)
        self.weibo_layout.addRow(self.weibo_button)
        self.weibo_layout.addRow(self.weibo_result)

        self.layout.addWidget(self.qq_group)
        self.layout.addWidget(self.phone_group)
        self.layout.addWidget(self.weibo_group)

        self.qq_query_button.clicked.connect(self.on_qq_query)
        self.phone_query_button.clicked.connect(self.on_phone_query)
        self.weibo_button.clicked.connect(self.on_weibo_query)

        # Change the style of the application
        QApplication.setStyle(QStyleFactory.create('Fusion'))

        # Change the color of the application
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        QApplication.setPalette(palette)

        # Change the font of the application
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        QApplication.setFont(font)

    # ... Rest of your MainWindow class ...
        self.setWindowTitle("隐私查询软件")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.qq_label = QLabel("QQ查绑 请输入要查询的QQ:")
        self.qq_input = QLineEdit()
        self.qq_query_button = QPushButton("查询QQ号码")
        self.qq_result = QLabel()

        self.phone_label = QLabel("手机号反查 请输入手机号:")
        self.phone_input = QLineEdit()
        self.phone_query_button = QPushButton("查询手机号")
        self.phone_result = QLabel()

        self.weibo_label = QLabel("微博查绑 请输入微博ID")
        self.weibo_input = QLineEdit()
        self.weibo_button = QPushButton("查询微博ID")
        self.weibo_result = QLabel()

        widgets = [self.qq_label, self.qq_input, self.qq_query_button, self.qq_result,
                   self.phone_label, self.phone_input, self.phone_query_button, self.phone_result,
                   self.weibo_label, self.weibo_input, self.weibo_button, self.weibo_result]

        for widget in widgets:
            self.layout.addWidget(widget)

        self.qq_query_button.clicked.connect(self.on_qq_query)
        self.phone_query_button.clicked.connect(self.on_phone_query)
        self.weibo_button.clicked.connect(self.on_weibo_query)

    def on_qq_query(self):
        qq_number = self.qq_input.text()
        if qq_number == "":
            self.qq_result.setText("未检测到用户输入")
        else:
            if len(qq_number) > 10:
                self.qq_result.setText("你输入的数据太长了，不是QQ号")
            else:
                self.qq_result.setText("查询中……")
                self.thread = QueryThread('https://zy.xywlapi.cc/qqcx2023?qq=' + qq_number)
                self.thread.result_signal.connect(self.qq_query_result)
                self.thread.start()

    def qq_query_result(self, response):
        qq_number = self.qq_input.text()
        if "查询成功" in response:
            result = "qq: {}\n电话号码: {} {}".format(qq_number, response[40:51], response[66:73] + "\n内容已复制")
            pyperclip.copy(result.replace("\n内容已复制",""))
            self.qq_result.setText(result)
        elif "没有找到" in response:
            self.qq_result.setText("qq: {} 没有找到电话号码".format(qq_number))

    def on_phone_query(self):
        phone_number = self.phone_input.text()
        if phone_number == "":
            self.phone_result.setText("未检测到用户输入")
        else:
            if len(phone_number) > 11:
                self.phone_result.setText("你输入的数据太长了，不是手机号")
            else:
                self.phone_result.setText("查询中……")
                self.thread = QueryThread(f"{xywlapi}/qqphone?phone=" + phone_number)
                self.thread.result_signal.connect(self.phone_query_result)
                self.thread.start()

    def phone_query_result(self, response):
        phone_number = self.phone_input.text()
        if "查询成功" in response:
            result = "电话: {}\n对应qq号码是: {}".format(phone_number, response[37:47] + "\n内容已复制")
            pyperclip.copy(result.replace("\n内容已复制",""))
            self.phone_result.setText(result)
        elif "没有找到" in response:
            self.phone_result.setText("电话: {} 没有找到qq号码".format(phone_number))

    def on_weibo_query(self):
        weibo_id = self.weibo_input.text()
        if weibo_id == "":
            self.weibo_result.setText("未检测到用户输入")
        else:
            self.weibo_result.setText("查询中……")
            self.thread = QueryThread(f"{xywlapi}/wbapi?id=" + weibo_id)
            self.thread.result_signal.connect(self.weibo_query_result)
            self.thread.start()

    def weibo_query_result(self, response):
        weibo_id = self.weibo_input.text()
        if "查询成功" in response:
            data = json.loads(response)
            result = "微博ID: {} 的电话号码是：{} {} 内容已复制".format(weibo_id, data["phone"], data["phonediqu"])
            pyperclip.copy(result.replace(" 内容已复制",""))
            self.weibo_result.setText(result)
        elif "没有找到" in response:
            self.weibo_result.setText("微博ID: {} 没有找到电话号码".format(weibo_id))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    xywlapi = decoded_text = base64.b64decode("aHR0cHM6Ly96eS54eXdsYXBpLmNj").decode('utf-8')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
