import serial

def send_message(ser):
    #设置需要发送的数据
    words = [0x01,0x04,0x01,0xA1,0x00,0x17,0xE0,0x1A]

    while 1:
        ser.write(words)

def receive_message(ser):
    pass


if __name__ == '__main__':

    #创建串口实例
    ser = serial.Serial("COM5",115200,timeout=0.1)


    #连接串口
    try:
        ser.open()
    except Exception:
        print("串口打开失败")

    print("打开成功，串口号COM5")
    words = [0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A]
    while 1:
        ser.write(words)








