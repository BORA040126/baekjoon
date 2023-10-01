a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)

c.sort()
for i in range(len(c)):
    print(c[i])
