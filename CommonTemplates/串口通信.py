import serial
import time
# 十六进制显示
#将输入的二进制数据流转换为16进制
def hexShow(data):
    arr =''
    dlen = len(data)
    for i in range(dlen):
        mid = str(int(data[i],16))
        arr +=mid+' '
    print(mid)

if __name__ == '__main__':
    serial = serial.Serial("COM6", 115200, timeout=0.01)
    while(1):
        serial.write([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A])
        data = serial.read_all()
        time.sleep(0.5)
        #将bytes16进制的数字转换为10进制数字
        try:
            print(hexShow(data))
        except Exception:
            pass