a=int(input())
f=[]
g=[]
for i in range(a):
    b=input()
    c=[]
    for j in b:
        c.append(j)
    d=set(c)
    e=""
    h=list(d)
    for i in range(len(h)):
        e=h[i]+e
    g.append(e)

for i in range(a):
    print(g[i])
