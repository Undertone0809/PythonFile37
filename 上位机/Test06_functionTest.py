
def method1(a,b,c,*args):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("*agrs=",args)

def method2(a,b,*args1,**args2):
    print("a=", a)
    print("b=", b)
    print("*agrs1=", args1)
    print("*agrs2=", args2)


def method3(*args1, **args2):
    print("*agrs1=", args1)
    print("*agrs2=", args2)


if __name__ == '__main__':
    method1(1,2,3,4,5)
    '''
    a= 1
    b= 2
    c= 3
    *agrs= (4, 5)
    '''

    method2(1, 2, 3, 4, 5,name="jack")
    '''
    a= 1
    b= 2
    *agrs1= (3, 4, 5)
    *agrs2= {'name': 'jack'}
    '''

    method2(1,2,3,num1=1212,num2=22323)
    '''
    a= 1
    b= 2
    *agrs= (3,)
    *agrs= {'num1': 1212, 'num2': 22323}
    '''

    method3(1,None,"a","b",num1=222,name="jack")
    '''
    *agrs1= (1, None, 'a', 'b')
    *kwagrs= {'num1': 222, 'name': 'jack'}
    '''

    #method3(1,num1=222,name="jack",None,2