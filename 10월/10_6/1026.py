a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
b.sort()
c.sort(reverse=True)
d=0
for i in range(a):
    d=d+b[i]*c[i]
print(d)