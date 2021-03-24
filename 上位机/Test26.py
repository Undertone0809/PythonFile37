if __name__ == '__main__':
    #在字符串中添加变量
    arr = []
    for i in range(10):
        arr.append(i)

    for i in range(10):
        data = "now is "
        data1 ="here "
        data2 = data1 + data
        data3 =data2 + str(arr[i]) +" " + str(arr[i+1])
        print(data3)