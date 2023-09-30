b=[]
while(1):
    a=list(map(int,input().split()))
    if sum(a)==0:
        break
    else:
        if a[0]%a[1]==0:
            b.append("multiple")
        elif a[1]%a[0]==0:
            b.append("factor")
        else:
            b.append("neither")
for i in b:
    print(i)