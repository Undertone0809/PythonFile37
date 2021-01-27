# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 02:19
# @Author  : Zeeland
# @File    : SendInfo.py
# @Software: PyCharm
"""
该抽象类是所有发送特定信息方法的父类
该抽象类定义了以下几个抽象方法
(1)发送特定信息的方法@send_message
(2)返回信息码的方法@return_code
(3)调用button的方法@button_clicked
(4)发送特定信息并将发送的信息码打印到执行输出Text框中的方法@sp_message,为(1)方法的扩展

以下测试SendVibration可行性的代码：
if __name__ == '__main__':
    ser = serial.Serial()
    try:
        # 传入参数
        ser = serial.Serial("COM1", 115200, timeout=0.01)
        if ser.isOpen():
            print("端口已经打开")
        #调用SendVibration
        s =SendVibration()
        s.send_sessage(ser)
    except Exception as e:
        print('端口连接失败,错误原因：\n', e)

"""

import abc
import time
import serial
"""


重写了方法，将部分方法修改为内置方法，待修改......


"""
class SendInfo(metaclass=abc.ABCMeta):

    """
    调用该方法可以发送指定信息码
    该方法传入一个serial对象
    """
    @abc.abstractmethod
    def send_sessage(self,ser):
        pass


    """
    调用该方法返回信息码
    """
    @abc.abstractmethod
    def return_code(self):
        pass


    """
    该方法传入一个button的引用，为该button创建clicked之后发送信息的方法
    """
    @abc.abstractmethod
    def button_clicked(self,button):
        pass

    """
    该方法为发送特定信息并将发送的信息码打印到执行输出Text框中的方法@sp_message
    该方法传入一个serial对象和一个QTextBrowser控件，在该Text控件输出发送信息码
    """
    @abc.abstractmethod
    def sp_message(self,ser,QTextBorwser):
        pass


    """
    十六进制显示
    输入一个数据类型为<class 'bytes'>bytes数据流
    该方法用于给子类的send_message方法提供16进制转码
    """
    def hexShow(self,argv):
        try:
            result = ''
            hLen = len(argv)
            for i in range(hLen):
                hvol = argv[i]

                # 不足两位，则补0,以16进制表示bytes数据流
                hhex = '%02x' % hvol
                result += hhex + ' '
            return result
        except Exception as e:
            print("---异常---：", e)



"""
该类为发送振动信息类，该继承抽象类SendMessage
该类提供了以下方法
(1)发送特定信息的方法@send_message
(2)返回信息码的方法@return_code
(3)调用button的方法@__button_clicked__
"""
class SendVibration(SendInfo):

    """
    该方法传入一个端口对象，像该端口输出振动信息
    """
    def send_sessage(self,ser):
        # 传入一个16进制数组
        ser.write(bytes([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A]))

        # 打印输出的16进制信息
        #print(self.hexShow(ser.read_all()))


    """
    该方法无需传入参数，返回一个16进制的str数组，为该类的信息码
    """

    def return_code(self):
        return '01 04 01 A1 00 17 E0 1A'

    """
    该方法传入一个button的引用，为该button创建clicked之后发送信息的方法
    """
    def __button_clicked__(self,button):
        button.clicked.connect(self.send_sessage())


    """
    该方法传入一个serial对象和一个QTextBrowser控件，在该Text控件输出发送信息码
     """
    def sp_message(self,ser,QTextBrowser):
        ser.write(bytes([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A]))
        QTextBrowser.append(self.return_code())





"""
该类为发送Modbus类，该继承抽象类SendMessage
该类提供了以下方法
(1)发送特定信息的方法@send_message
(2)返回信息码的方法@return_code
(3)调用button的方法@button_clicked
"""
class SendModbus(SendInfo):

    """
    该方法传入一个端口对象，像该端口输出信息查看 modbus设备地址
    """
    def send_sessage(self,ser):
        # 传入一个16进制数组
        ser.write(bytes([0x01,0x03,0x00,0x64,0x00,0x01,0xC5,0XD5]))

        # 打印输出的16进制信息
        #print(self.hexShow(ser.read_all()))


    """
    该方法无需传入参数，返回一个16进制的str数组，为该类的信息码
    """

    def return_code(self):
        return  '01 03 00 64 00 01 C5 D5'

    """
    该方法传入一个button的引用，为该button创建clicked之后发送信息的方法
    """
    def button_clicked(self,button):
        button.clicked.connect(self.send_sessage())

    """
    该方法传入一个serial对象和一个QTextBrowser控件，在该Text控件输出发送信息码
    """
    def sp_message(self, ser, QTextBrowser):
        ser.write(bytes([0x01,0x03,0x00,0x64,0x00,0x01,0xC5,0XD5]))
        QTextBrowser.append(self.return_code())
