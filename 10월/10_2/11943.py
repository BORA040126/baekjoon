a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a[0]+b[1]
d=a[1]+b[0]

if c>d:
    print(d)
else:
    print(c)
