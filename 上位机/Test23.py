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


p1 = person(name="小明", age="18")
p2 = person(age="18",name="小明")
p3 = person(age="18")
p4 = person(name="小明")



class student:
    def __init__(self,age,name):
        self.age = age
        self.name =name
        self.printMessage()

    def printMessage(self):
        print(self.age)
        print(self.name)


if __name__ == '__main__':
    jack =student(name="jack", age="22")
