# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 22:23
# @Author  : Zeeland
# @File    : FunEdit.py
# @Software: PyCharm

from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QMessageBox
from UiForm import Ui_Form
import sys,time,pygame
from test_demo import Operate


import math
'''编译定义类'''
class FunEdit(QWidget,Ui_Form):
    '''初始化各方面信息'''
    def __init__(self):
        super(FunEdit, self).__init__()
        self.setupUi(self)#Ui初始化
        self.init()
        pygame.init()  # 初始化音乐播放装置，初始化后才可以使用
        self.operate = Operate()


    '''该方法用于信号与槽的绑定'''
    def init(self):
        self.btn_readMusic.clicked.connect(self.readMusic)
        self.btn_start.clicked.connect(self.start)


    '''读取音频'''
    def readMusic(self):
        #读取特定格式的文件,传入一个self,"标题名","初始显示文件夹的路径","特定格式(以两个分号区分)"
        #该方法返回一个Tuple,分别为str类型的路径名和file的type(eg:MP3)
        self.fdir,self.ftype =QFileDialog.getOpenFileName(self,"Open File","","Mp3(*.mp3);;Wav(*.wav)")

        # 判断是否为空路径，如果为空路径，则不能加载音频，否则会闪退
        if self.fdir=="":
            print("没有选择文件")
            return

        print(self.fdir)

        #对fdir进行处理
        self.devide()

        self.track =pygame.mixer.music.load(str(self.fdir))#加载音频文件(放入缓存池)
        self.label_DirMessage.setText(str(self.fdir))


    def devide(self):
        self.arr =self.fdir.split("/")
        #倒序输出
        # self.parent_dir=self.arr[self.arr.len-1]
        print("*"*60)
        print(self.arr)
        self.sub_dirs=self.arr[len(self.arr)-2]+"/"
        print('sub_dirs:',self.sub_dirs)
        self.parent_dir=""
        for i in range(len(self.arr)-2):
            self.parent_dir+=self.arr[i]
            if i != len(self.arr)-3:
                self.parent_dir+="/"
        self.parent_dir="r"+self.parent_dir

        # 向operate中传入参数
        self.operate.sub_dirs = [self.sub_dirs]
        self.operate.parent_dir = self.parent_dir

        print('parent_dir:',self.parent_dir)
        print("*"*60)


    def start(self):
        self.label_AnsMessage.setText(str(self.operate.ans[0]))



'''主方法运行入口'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FunEdit()
    win.show()
    sys.exit(app.exec())