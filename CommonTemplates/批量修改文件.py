# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 17:47
# @Author  : Zeeland
# @File    : 批量修改文件.py
# @Software: PyCharm
import os,sys,re


def renameall():
    fileList = os.listdir(r"C:\Users\86132\Desktop\here")  # 待修改文件夹
    print("修改前：" + str(fileList))

    currentpath = os.getcwd()  # 得到进程当前工作目录
    os.chdir(r"C:\Users\86132\Desktop\here")  # 将当前工作目录修改为待修改文件夹的位置
    num = 1  # 名称变量
    for fileName in fileList:  # 遍历文件夹中所有文件
        pat = ".+\.(jpg|png|gif)"  # 匹配文件名正则表达式
        pattern = re.findall(pat, fileName)  # 进行匹配
        os.rename(fileName, ('物理实验02第'+str(num) + '张.' + pattern[0]))  # 文件重新命名
        #其中pattern[0]为后缀格式
        num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(currentpath)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    print("*"*60)
    print("修改后：" + str(os.listdir(r"C:\Users\86132\Desktop\here")))  # 输出修改后文件夹中包含的文件


if __name__ == '__main__':
    # 批量修改文件名
    # 批量修改图片文件名
    renameall()