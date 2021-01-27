def fibs(n):
    result=[0,1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result
'''
def fibs1(n):
    arr =[0]*n
    arr[0] =0
    arr[1] =1
    for i in range(n-1):
        arr[n] = arr[n-1] + arr[n-2]
    return arr
print(fibs1(5))
'''



def fibs2(n):
    a,b = 0,1
    arr = [0,1]
    for i in range(n-1):
            a,b = b,a+b
            arr.append(b)
    print(arr)
fibs2(10)

def fibs3(n):
    lis =[]
    for i in range(n):
        if i ==1 or i ==0:
            lis.append(1)
        else:
            lis.append(lis[i-2]+lis[i-1])
    print(lis)
fibs3(10)