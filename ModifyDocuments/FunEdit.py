# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 00:05
# @Author  : Zeeland
# @File    : FunEdit.py
# @Software: PyCharm
from UI import Ui_Form
from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog
import sys

class FunEdit(Ui_Form,QWidget):
    def __init__(self):
        super(FunEdit, self).__init__()
        self.setupUi(self)
        self.init()

    '''绑定事件'''
    def init(self):
        self.btn_openFile.clicked.connect(self.openFile)

    '''打开文件'''
    def openFile(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        print(directory1)


'''主方法运行入口'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FunEdit()
    win.show()
    sys.exit(app.exec())