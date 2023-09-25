a,b=map(int,input().split()) 
c=list(map(int, input().split()))
g=0
h=[]
for i in range(b):
    e,f=map(int,input().split())
    g=0
    if e==f:
        h.append(1)
    else:
        g=sum(c[e-1:f])
        h.append(g)

for i in range(len(h)):
    print(h[i])
