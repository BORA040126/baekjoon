import math
a,b,c=map(int, input().split())
f=[]
d=math.sqrt(b**2+c**2)
for i in range(a):
    e=int(input())
    if e>d:
        f.append("NE")
    else:
        f.append("DA")
for j in range(a):
    print(f[j])