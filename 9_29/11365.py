b=[]
while(1):
    a=list(map(int,input().split()))
    a.sort()
    if sum(a)==0:
        break
    else:
        if a[2]**2==a[0]**2+a[1]**2:
            b.append("right")
        else:
            b.append("wrong")
for i in range(len(b)):
    print(b[i])
