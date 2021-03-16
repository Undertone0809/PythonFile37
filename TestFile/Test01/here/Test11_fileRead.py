# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 16:02
# @Author  : Zeeland
# @File    : Test11_fileRead.py
# @Software: PyCharm
if __name__ == '__main__':
    try:
        #创建实例对象
        f1 = open('sensor.txt', 'r')
        f2 = open('earpa001.txt','w+')
        #读取文件
        data =f1.read()
        '''
        data:
        2016/5/31 0:05,vawelon001,1,1
        2016/5/31 0:05,earpa001,1,7
        2016/5/31 0:05,vawelon001,5,1
        2016/5/32 0:05,earpa001,3,6
        2016/5/31 0:05,earpa001,1,5
        2016/5/31 0:05,vawelon001,1,1
        2016/5/32 0:05,earpa001,2,3
        2016/5/31 0:05,vawelon001,1,2
        2016/5/31 0:05,earpa001,1,2
        2016/5/31 0:05,vawelon001,1,2
        2016/5/31 0:05,earpa001,1,2
        2016/5/32 0:05,earpa001,3,6
        2016/5/31 0:05,earpa001,1,5
        2016/5/32 0:05,earpa001,3,6
        2016/5/31 0:05,earpa001,1,5
        2016/5/31 0:05,vawelon001,1,1
        2016/5/32 0:05,earpa001,2,3
        2016/5/31 0:05,vawelon001,1,2
        2016/5/32 0:05,earpa001,2,3
        '''
        #将文件中的所有元素转换为数组
        a =data.split("\n")
        '''
        a=['2016/5/31 0:05,vawelon001,1,1', '2016/5/31 0:05,earpa001,1,7', '2016/5/31 0:05,vawelon001,5,1', '2016/5/32 0:05,earpa001,3,6', '2016/5/31 0:05,earpa001,1,5', '2016/5/31 0:05,vawelon001,1,1', '2016/5/32 0:05,earpa001,2,3', '2016/5/31 0:05,vawelon001,1,2', '2016/5/31 0:05,earpa001,1,2', '2016/5/31 0:05,vawelon001,1,2', '2016/5/31 0:05,earpa001,1,2', '2016/5/32 0:05,earpa001,3,6', '2016/5/31 0:05,earpa001,1,5', '2016/5/32 0:05,earpa001,3,6', '2016/5/31 0:05,earpa001,1,5', '2016/5/31 0:05,vawelon001,1,1', '2016/5/32 0:05,earpa001,2,3', '2016/5/31 0:05,vawelon001,1,2', '2016/5/32 0:05,earpa001,2,3']
        '''

        #循环数组
        #每个i就是一条信息，eg:2016/5/32 0:05,earoa001,3,6
        for i in a:
            '''
            i:
            2016/5/31 0:05,vawelon001,1,1
            2016/5/31 0:05,earpa001,1,7
            2016/5/31 0:05,vawelon001,5,1
            2016/5/32 0:05,earpa001,3,6
            2016/5/31 0:05,earpa001,1,5
            2016/5/31 0:05,vawelon001,1,1
            2016/5/32 0:05,earpa001,2,3
            2016/5/31 0:05,vawelon001,1,2
            2016/5/31 0:05,earpa001,1,2
            2016/5/31 0:05,vawelon001,1,2
            2016/5/31 0:05,earpa001,1,2
            2016/5/32 0:05,earpa001,3,6
            2016/5/31 0:05,earpa001,1,5
            2016/5/32 0:05,earpa001,3,6
            2016/5/31 0:05,earpa001,1,5
            2016/5/31 0:05,vawelon001,1,1
            2016/5/32 0:05,earpa001,2,3
            2016/5/31 0:05,vawelon001,1,2
            2016/5/32 0:05,earpa001,2,3
            '''
            #将里面的每个元素都转换为数组,通','分离数组
            c =i.split(",")
            '''
            c:
            ['2016/5/31 0:05', 'vawelon001', '1', '1']
            ['2016/5/31 0:05', 'earpa001', '1', '7']
            ['2016/5/31 0:05', 'vawelon001', '5', '1']
            ['2016/5/32 0:05', 'earpa001', '3', '6']
            ['2016/5/31 0:05', 'earpa001', '1', '5']
            ['2016/5/31 0:05', 'vawelon001', '1', '1']
            ['2016/5/32 0:05', 'earpa001', '2', '3']
            ['2016/5/31 0:05', 'vawelon001', '1', '2']
            ['2016/5/31 0:05', 'earpa001', '1', '2']
            ['2016/5/31 0:05', 'vawelon001', '1', '2']
            ['2016/5/31 0:05', 'earpa001', '1', '2']
            ['2016/5/32 0:05', 'earpa001', '3', '6']
            ['2016/5/31 0:05', 'earpa001', '1', '5']
            ['2016/5/32 0:05', 'earpa001', '3', '6']
            ['2016/5/31 0:05', 'earpa001', '1', '5']
            ['2016/5/31 0:05', 'vawelon001', '1', '1']
            ['2016/5/32 0:05', 'earpa001', '2', '3']
            ['2016/5/31 0:05', 'vawelon001', '1', '2']
            ['2016/5/32 0:05', 'earpa001', '2', '3']
            '''
            #如果c里面存在vawelon001,则储存到一个新的文件中
            if c[1]=='earpa001':
                #写文件
                #i.strip是删除最后一行的空行，不用i.strip()的话最后一行会空出来
                f2.write(i.strip())
                f2.write('\n')


    finally:
        if f1:
            f1.close()
        if f2:
            f2.close()