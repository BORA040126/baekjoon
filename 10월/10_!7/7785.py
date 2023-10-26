a=int(input())
b=[]
for i in range(a):
    c=list(map(str,input().split()))
    if c[1]=="enter":
        b.append(c[0])
    else:
        b.remove(c[0])
b.sort(reverse=True)
for j in b:
    print(j)