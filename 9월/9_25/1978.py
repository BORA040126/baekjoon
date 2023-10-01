a=int(input())
b=list(map(int, input().split()))
d=0
e=0
for i in range(len(b)):
    c=0
    if b[i]==1:
            continue
    else:
        for j in range(2,b[i]):
            d=0
            d=b[i]%j
            if d==0:
                c+=1
        if c==0:
            e+=1
print(e)