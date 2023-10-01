a=int(input())
b=list(map(int, input().split()))
c=int(input())
d=list(map(int, input().split()))
for i in range(len(d)):
    if d[i] in b:
        print("1",end=" ")
    else:
        print("0", end=" ")