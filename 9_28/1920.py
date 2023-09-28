a=int(input())
b=set(map(int,input().split(" ")))
c=int(input())
d=list(map(int,input().split(" ")))
e=[]
for i in d:
    if i in b:
        e.append(1)
    else:
        e.append(0)
for i in range(len(e)):
    print(e[i])