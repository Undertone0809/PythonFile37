# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 02:19
# @Author  : Zeeland
# @File    : SendInfo.py
# @Software: PyCharm

"""
该类为连接串口的类，提供了以下方法：
(1)连接串口的方法connect_COM
(2)通过pushbutton连接串口的方法bc_COM
"""

import serial

class Connection:
    def __int__(self):
        super().__init__()
        #ser为串口对象



    """
    该方法直接发送串口连接请求
    """
    def connect_COM(self):
        try:
            self.ser = serial.Serial("COM1", 115200, timeout=0.01)
            print("串口打开成功")
        except Exception as e:
            print("串口打开失败")

    """
    该方法传入一个pushbutton,通过clicked来发送串口连接请求
    """
    def __bc_COM__(self,button):
        button.clicked.connect(self.connect_COM())