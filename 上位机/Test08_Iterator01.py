# DelelopmentTime: 2021/1/7  14:56
dic={'a':1,'b':2,'c':3}
iter_dic=dic.__iter__() #得到迭代器对象，迭代器对象即有__iter__又有__next__，但是：迭代器.__iter__()得到的仍然是迭代器本身
iter_dic.__iter__() is iter_dic #True
