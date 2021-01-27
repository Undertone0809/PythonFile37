# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 06:19
# @Author  : Zeeland
# @File    : Test21.py
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class FirstMainWindow(QMainWindow):
    # 初始化方法保证MainWindow是主窗口
    def __init__(self):
        super(FirstMainWindow,self).__init__()

        self.setWindowTitle("this is a title")

        self.resize(400,300)

        #设置消息栏
        self.status = self.statusBar()

        self.status.showMessage('only 5 seconds',5000)

if __name__ == '__main__':
    app  =QApplication(sys.argv)

    main =FirstMainWindow()

    main.show()

    sys.exit(app.exec_())