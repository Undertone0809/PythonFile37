# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 15:30
# @Author  : Zeeland
# @File    : 格式化输出时间.py
# @Software: PyCharm
import time

if __name__ == '__main__':
    local_time = time.localtime(time.time())
    date_format_localtime = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    print(date_format_localtime)