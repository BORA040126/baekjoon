a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b.append(c)

d=list(set(b))
d.sort()

for i in range(len(d)):
    print(d[i])