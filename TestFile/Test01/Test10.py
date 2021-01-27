import serial
import time
import sys
import logging

#定义一个发送的方法
def sendMessage():
    # 创建端口对象
    ser = serial.Serial()
    try:
        # 传入参数
        ser = serial.Serial("COM1", 115200, timeout=0.01)
        # 连续发送信息
        while 1:
            ser.write([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A])

            # 设置发送间隔时间为0.3s
            time.sleep(0.3)

            # 打印输出的16进制信息
            print(hexShow(ser.read_all()))
            # print(ser.read_all().decode(),'ascii')

    except Exception as e:
        print('端口连接失败,错误原因：\n', e)


def hexShow(argv):
    try:
        result = ''

        hLen = len(argv)
        for i in range(hLen):
            hvol = argv[i]
            hhex = '%02x' % hvol
            result += hhex + ' '


        logging.info('Led Read:%s', result)
        return result
    except Exception as e:
        print("---异常---：", e)



if __name__ == '__main__':
    sendMessage()
    sys.exit()