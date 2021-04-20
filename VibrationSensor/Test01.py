import pymysql

if __name__ == '__main__':
    try:
        # 连接数据库
        conn = pymysql.connect(host='rm-bp1o0649d1hoda9z2wo.mysql.rds.aliyuncs.com', user='user02', password='Lzn123456',
                               db='vibrationsensor', port=3306, charset='utf8')
        print('连接数据库成功！')
        cursor = conn.cursor()

    except Exception as e:
        print(e)

    # "select * from t_vibrationsensor02"
    sql = 'select * from t_vibrationsensor02  order by id desc  limit 1'
    cursor.execute(sql)
    data1 = cursor.fetchone()
    while True:
        cursor.execute(sql)
        data2 = cursor.fetchone()
        if data1 == data2:
            pass
        else:
            data1 = data2
            print(data2)