a=int(input())
b=[]
for i in range(a):
    c=list(map(int,input().split()))
    c.sort(reverse=True)
    b.append(c[2])

for i in b:
    print(i)