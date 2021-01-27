# -*- coding: utf-8 -*-
# @Time    : 2021/1/9 21:54
# @Author  : Zeeland
# @File    : Test12.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Button")
        text = QTextEdit('text')
        text.resize(text.sizeHint())
        text.move(30,30)

        btn =QPushButton('button',self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui =UI()
    sys.exit(app.exec_())
