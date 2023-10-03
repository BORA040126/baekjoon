num,total=map(int,input().split())
count=0
a=[]
for i in range(num):
    b=int(input())
    a.append(b)

a.sort(reverse=True)

for j in range(len(a)):
    c=0
    c=total//a[j]
    count+=c
    total=total-(c*a[j])

print(count)