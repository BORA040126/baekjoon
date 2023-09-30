b=[]
while(1):
    a=list(map(int, input().split()))
    if sum(a)==0:
        break
    else:
        b.append(sum(a))

for i in b:
    print(i)