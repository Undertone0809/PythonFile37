t = int(input())
for i in range(t):
    m = input()
    m = m.split()
    n1 = int(m[0])
    n2 = int(m[1])
    k = int(m[2])
    m1 = n1//k
    m2 = n2//k
    print(m1*m2)
