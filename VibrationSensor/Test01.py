# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 20:02
# @Author  : Zeeland
# @File    : Test01.py
# @Software: PyCharm
import time
if __name__ == '__main__':
    file = open('传感器data.txt','r')
    data =file.read()
    print(data)


    # 格式化年月日时分秒
    # local_time = time.localtime(time.time())
    # date_format_localtime = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    # print("格式化时间之后为:%s" % date_format_localtime)


