# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 19:51
# @Author  : Zeeland
# @File    : Connection.py
# @Software: PyCharm
"""
该测试用于测试连接起与振动传感器之间的通讯关系，并且接受到振动数据
    是一个基础的测试模块
"""

import serial
import sys
import time


# 十六进制显示
#argv为<class 'bytes'>bytes数据流
def hexShow(argv):
    try:
        result = ''
        hLen = len(argv)
        for i in range(hLen):
            hvol = argv[i]

            #不足两位，则补0,以16进制表示bytes数据流
            hhex = '%02x' % hvol
            result += hhex + ' '
        return result
    except Exception as e:
        print("---异常---：", e)


if __name__ == '__main__':

    #创建端口对象
    ser =serial.Serial()
    try:
        #传入参数
        ser = serial.Serial("COM1", 115200, timeout=0.01)

        count = 0
        #连续发送信息
        while 1:
            #传入一个16进制数组
            ser.write(bytes([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A]))

            #设置发送间隔时间为0.3s
            time.sleep(1)

            #打印输出的16进制信息
            print(hexShow(ser.read_all()))

            print("发送了",count,"次信息")
            count = count + 1


    except Exception as e:
        print('端口连接失败,错误原因：\n',e)
#关闭串口
sys.exit()