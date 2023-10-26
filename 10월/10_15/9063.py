a=int(input())
b=[]
c=[]
for i in range(a):
    d,e=map(int,input().split())
    b.append(d)
    c.append(e)

f=max(b)-min(b)
g=max(c)-min(c)
print(f*g)