# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 20:36
# @Author  : Zeeland
# @File    : Test27_RdsMysqlConnectTest.py
# @Software: PyCharm
import pymysql

if __name__ == '__main__':
    try:
        # 连接数据库
        conn = pymysql.connect(host='rm-bp1o0649d1hoda9z2wo.mysql.rds.aliyuncs.com', user='user01', password='Lzn123456',
                               db='vibrationsensor', port=3306, charset='utf8')
        print('连接数据库成功！')
        cursor = conn.cursor()

    except Exception as e:
        print(e)
