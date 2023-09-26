a=int(input())
d=[]
for i in range(a):
    b,c,e=map(int,input().split(" "))
    d.append(b*(e-1)+c)
for i in range(len(d)):
    print(d[i])
