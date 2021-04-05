class person:
    def __init__(self,**args):
        print("调用了初始化方法")
        self.name = args.get("name")
        self.age =args.get("age")
        self.printMessage()
        self.method(**args)

    def printMessage(self):
        print(self.age)
        print(self.name)


    def method(self,**args):
        self.name = args.get("name")


zhangsan =person(name="小明",age="18")
jack = person(name="jack")
something =person(name="jacasdask")

print("*"*60)
print(something.name)
