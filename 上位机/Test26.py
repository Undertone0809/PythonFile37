import pymysql

db = pymysql.connect(host="localhost", user="root", password="lzn123", database="mysql")

cursor = db.cursor()  # 数据库操作
