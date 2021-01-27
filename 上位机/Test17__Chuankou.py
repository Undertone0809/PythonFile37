# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 01:13
# @Author  : Zeeland
# @File    : Test17__Chuankou.py
# @Software: PyCharm
import serial
import sys
input_s ='01 02 03 04 05 06'
num = int(input_s[0:2], 16)

#去除第一个，以16进制的方式
print(num)

input_s = input_s[2:].strip()

print(input_s)
print('______________________________')

#该方法输入一个16进制字符串
#返回一个用于二进制的数据处理的数据类型
def method(input_s):
    send_list= []
    while input_s != '':
        # 输入16进制的字符
        #取出数组中前面两位字符
        #将字符按照16进制转换为int数据类型
        num = int(input_s[0:2], 16)
        print(num)

        #提取数组中两位数后面的数字,然后再去除左右两边的空白
        input_s = input_s[2:].strip()

        send_list.append(num)


    input_s = bytes(send_list)
    print(input_s)#b'\x02\x03\x04\x05\x06'
    print(send_list)

method(input_s)
print('-----------------------------')
port_list = list(serial.tools.list_ports.comports())

# 串口检测
def port_detect(self):
    # 检测所有存在的串口 将信息存在字典中
    self.port_dict = {}
    # serial.tools.list_ports.comports()返回计算机上所有的port口信息
    # 将其存在列表中
    port_list = list(serial.tools.list_ports.comports())
    # 清除下拉列表中已有的选项
    self.sset_cb_choose.clear()
    for port in port_list:
    	# 添加到字典里
        self.port_dict["%s" % port[0]] = "%s" % port[1]
        # 添加到下拉列表选项
        self.sset_cb_choose.addItem(port[0] + '：' + port[1])
    if len(self.port_dict) == 0:
        self.sset_cb_choose.addItem('无串口')
	#self.sset_btn_open.setEnabled(True)


print(port_detect())
sys.exit()