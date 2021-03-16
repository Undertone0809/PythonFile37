# DelelopmentTime: 2021/1/7  14:30
# coding = utf-8
import time
import serial

if __name__ == '__main__':
    # 打开串口，设置串口的端口和波特率
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = "COM5"#注意，只能为COM%d

    # 并检查是否成功打开端口
    try:
        ser.open()
    except Exception:
        print('未检测到端口，程序结束')

    #查看串口的名称
    print('串口名称为:',ser.portstr)



    '''
    定时发送
    '''

    #定义想要发送的内容
    words = [0x01,0x04,0x01,0xA1,0x00,0x17,0xE0,0x1A]

    while(1):
        startTime = time.time()
        times = 256
        #当times不等于-1时会执行执行该部分
        #即while语句会执行256次
        while (times):
            times -= 1
            s = ser.write(words)
            mid =ser.read()
            print(mid)



        #执行
        endTime = time.time()
        print
        "use time: " + str(endTime - startTime)
        print("")

        #延迟5秒调用线程
        #time.sleep(5)
        print(ser.read(1))
        print(type(ser.read(1)))

    #关闭串口
    ser.close()


