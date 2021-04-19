# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 22:23
# @Author  : Zeeland
# @File    : FunEdit.py
# @Software: PyCharm

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
import sys, time, pygame

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 350)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 200, 471, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_readMusic = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_readMusic.setObjectName("btn_readMusic")
        self.horizontalLayout.addWidget(self.btn_readMusic)
        self.btn_start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 80, 160, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 80, 731, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_DirMessage = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_DirMessage.setObjectName("label_DirMessage")
        self.verticalLayout_2.addWidget(self.label_DirMessage)
        self.label_AnsMessage = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_AnsMessage.setObjectName("label_AnsMessage")
        self.verticalLayout_2.addWidget(self.label_AnsMessage)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_readMusic.setText(_translate("Form", "读取音频"))
        self.btn_start.setText(_translate("Form", "开始识别"))
        self.label_2.setText(_translate("Form", "音频路径:"))
        self.label.setText(_translate("Form", "输出结果:"))
        self.label_DirMessage.setText(_translate("Form", "暂无"))
        self.label_AnsMessage.setText(_translate("Form", "暂无"))


'''编译定义类'''


class FunEdit(QWidget, Ui_Form):
    '''初始化各方面信息'''

    def __init__(self):
        super(FunEdit, self).__init__()
        self.setupUi(self)  # Ui初始化
        self.init()
        pygame.init()  # 初始化音乐播放装置，初始化后才可以使用

    '''该方法用于信号与槽的绑定'''

    def init(self):
        self.btn_readMusic.clicked.connect(self.readMusic)
        self.btn_start.clicked.connect(self.start)

    '''读取音频'''

    def readMusic(self):
        # 读取特定格式的文件,传入一个self,"标题名","初始显示文件夹的路径","特定格式(以两个分号区分)"
        # 该方法返回一个Tuple,分别为str类型的路径名和file的type(eg:MP3)
        self.fdir, self.ftype = QFileDialog.getOpenFileName(self, "Open File", "", "Wav(*.wav);;Mp3(*.mp3)")

        # 判断是否为空路径，如果为空路径，则不能加载音频，否则会闪退
        if self.fdir == "":
            print("没有选择文件")
            return

        print(self.fdir)
        self.label_DirMessage.setText(str(self.fdir))
        # self.operate = Operate()
        # 对fdir进行处理
        self.devide()
        self.operate.run()

        self.track = pygame.mixer.music.load(str(self.fdir))  # 加载音频文件(放入缓存池)

    def devide(self):
        self.arr = self.fdir.split("/")
        # 倒序输出
        # self.parent_dir=self.arr[self.arr.len-1]
        print("*" * 60)
        print(self.arr)
        self.sub_dirs = self.arr[len(self.arr) - 2] + "/"
        print('sub_dirs:', self.sub_dirs)
        self.parent_dir = ""
        for i in range(len(self.arr) - 2):
            self.parent_dir += self.arr[i]
            if i != len(self.arr) - 3:
                self.parent_dir += "\\"
        # self.parent_dir="r"+self.parent_dir

        # 向operate中传入参数
        self.operate.sub_dirs = [self.sub_dirs]
        self.operate.parent_dir = self.parent_dir

        print('parent_dir:', self.parent_dir)
        print("*" * 60)

    def start(self):
        self.label_AnsMessage.setText(str(self.operate.ans[0]))


'''主方法运行入口'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FunEdit()
    win.show()
    sys.exit(app.exec())