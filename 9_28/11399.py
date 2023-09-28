a=int(input())
b=list(map(int,input().split(" ")))
b.sort()
e=[]

for i in range(a):
    c=0
    for j in range(i+1):
        c+=b[j]
    e.append(c)

print(sum(e))
