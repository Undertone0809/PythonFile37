# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 22:28
# @Author  : Zeeland
# @File    : Test23.py
# @Software: PyCharm
class person:
    def __init__(self,**agrs):
        print("调用了初始化方法")
        self.name = agrs.get("name")
        self.age =agrs.get("age")
        self.printMessage()

    def printMessage(self):
        print(self.age)
        print(self.name)


zhangsan =person(name="小明",age="18")