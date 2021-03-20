"""
该测试用于测试连接起与振动传感器之间的通讯关系，并且接受到振动数据
    是一个基础的测试模块
"""

import serial
import sys
import time


'''
将bytes的16进制表示转换为字符串10进制表示形式
'''
def hexShow(data):

    try:
        result = ''
        hLen = len(data)
        for i in range(hLen):
            mid = data[i]

            #不足两位，则补0,以16进制表示bytes数据流
            #hhex为单个元素

            hhex = '%02x' % mid
            result += hhex + ' '
        return result
    except Exception as e:
        print("---异常---：", e)
'''
将bytes类型的data转换为数组
'''
def hexArray(data):
    arr =[]
    try:
        result = ''
        hLen = len(data)
        for i in range(hLen):
            mid = data[i]

            # 不足两位，则补0,以16进制表示bytes数据流
            # hhex为单个元素
            hhex = '%02x' % mid
            arr.append(hhex)
        return arr
    except Exception as e:
        print("---异常---：", e)


if __name__ == '__main__':

    #创建端口对象
    ser =serial.Serial()
    try:
        #传入参数
        ser = serial.Serial("COM5", 115200, timeout=0.01)

        #连续发送信息
        while 1:
            #传入一个16进制数组
            ser.write(bytes([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A]))

            #恢复出厂配置
            #ser.write(bytes([0x01, 0x06, 0x00, 0x7F, 0x00, 0x01, 0x79, 0xD2]))
            #确认发送
            #ser.write(bytes([0x01, 0x06, 0x00, 0xC7, 0x00, 0x01, 0xF9, 0xF7]))
            #设置发送间隔时间为0.3s
            time.sleep(0.5)

            #打印输出的16进制信息
            print(hexShow(ser.read_all()))
            # print(hexArray(ser.read_all()))

    except Exception as e:
        print('端口连接失败,错误原因：\n',e)
#关闭串口
sys.exit()
