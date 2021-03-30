import time
if __name__ == '__main__':
    # 获取一个固定格式的时间:"0000-00-00 00:00:00"
    local_time = time.localtime(time.time())
    date_format_localtime = time.strftime('%Y-%m-%d %H:%M:%S %h:%i:%s', local_time)
    print("格式化时间之后为:%s" % date_format_localtime)
