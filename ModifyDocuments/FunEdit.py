# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 00:05
# @Author  : Zeeland
# @File    : FunEdit.py
# @Software: PyCharm
from UI import Ui_Form
from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog
import sys,os,re

class FunEdit(Ui_Form,QWidget):
    def __init__(self):
        super(FunEdit, self).__init__()
        self.setupUi(self)
        self.init()

    '''绑定事件'''
    def init(self):
        self.btn_openFile.clicked.connect(self.openFile)
        self.btn_transform.clicked.connect(self.transform)

    '''打开文件'''
    def openFile(self):
        self.file = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        self.fileList = os.listdir(self.file)
        for i in self.fileList:
            self.textBrowser_receive.append(i)


    def anayse(self):
        # self.fileList = os.listdir(r"C:\Users\86132\Desktop\here")  # 待修改文件夹
        print("修改前：" + str(self.fileList))

        currentpath = os.getcwd()  # 得到进程当前工作目录
        os.chdir(self.file)  # 将当前工作目录修改为待修改文件夹的位置
        num = 1  # 名称变量
        for fileName in self.fileList:  # 遍历文件夹中所有文件
            pat = ".+\.(jpg|png|gif)"  # 匹配文件名正则表达式
            pattern = re.findall(pat, fileName)  # 进行匹配
            m1=self.lineEdit_first.text()
            m2=self.lineEdit_second.text()
            os.rename(fileName, (m1 + str(num) + m2+"." + pattern[0]))  # 文件重新命名
            # 其中pattern[0]为后缀格式
            num = num + 1  # 改变编号，继续下一项
        print("---------------------------------------------------")
        os.chdir(currentpath)  # 改回程序运行前的工作目录
        sys.stdin.flush()  # 刷新
        self.fileList = str(os.listdir(self.file))
        print("修改后：" + self.fileList)  # 输出修改后文件夹中包含的文件

    def transform(self):
        self.anayse()
        for i in self.fileList:
            self.textBrowser_modify.append(i)


'''主方法运行入口'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FunEdit()
    win.show()
    sys.exit(app.exec())