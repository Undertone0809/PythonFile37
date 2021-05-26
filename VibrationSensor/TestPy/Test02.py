# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 19:22
# @Author  : Zeeland
# @File    : Test02.py
# @Software: PyCharm

"""
该类为连接串口的类，提供了以下方法：
(1)连接串口的方法connect_COM
(2)通过pushbutton连接串口的方法bc_COM
"""

import serial
import serial.tools.list_ports
class Connection:
    def __init__(self):
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

    # 检测串口的方法
    def port_check(self):
        port_list = list(serial.tools.list_ports.comports())
        # 添加到menu中
        for port in port_list:
            print(port)
        # 如果数组中没有内容
        if len(port_list) == 0:
            print('无串口')


if __name__ == '__main__':
    my_connection = Connection()
    my_connection.port_check()
