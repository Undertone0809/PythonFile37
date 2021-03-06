# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTimerTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 100, 131, 28))
        self.pushButton_start.setObjectName("pushButton_start")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 180, 72, 15))
        self.label.setObjectName("label")
        self.label_nowTime = QtWidgets.QLabel(Form)
        self.label_nowTime.setGeometry(QtCore.QRect(130, 180, 251, 16))
        self.label_nowTime.setText("")
        self.label_nowTime.setObjectName("label_nowTime")
        self.pushButton_stop = QtWidgets.QPushButton(Form)
        self.pushButton_stop.setGeometry(QtCore.QRect(220, 100, 121, 28))
        self.pushButton_stop.setObjectName("pushButton_stop")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_start.setText(_translate("Form", "开启定时调用"))
        self.label.setText(_translate("Form", "显示时间："))
        self.pushButton_stop.setText(_translate("Form", "关闭定时调用"))


from PyQt5.QtCore import QTimer, QDateTime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Edit(Ui_Form, QWidget):
    # 定义初始化进程
    def __init__(self):
        # 继承
        super().__init__()
        # 往空QWidget中放置UI内容
        self.setupUi(self)
        #初始化各种功能
        self.init()

    # 初始化各种功能
    def init(self):
        # 创建一个QTimer对象
        self.send_time = QTimer(self)

        # QTimer开始计时
        self.pushButton_start.clicked.connect(self.beginShowTime)

        # 给QTimer设定一个时间，每到达这个时间一次就会调用一次该方法
        self.send_time.timeout.connect(self.showTime)

        # QTimer关闭计时
        self.pushButton_stop.clicked.connect(self.stop)


    '''方法实现区'''
    def beginShowTime(self):
        # 设置QTimer开始计时，且设定时间为1000ms
        self.send_time.start(1000)

    # 显示时间的方法
    def showTime(self):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        self.timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # 在标签上显示时间
        self.label_nowTime.setText(self.timeDisplay)

    def stop(self):
        self.send_time.stop()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = Edit()
    myshow.show()
    sys.exit(app.exec_())
