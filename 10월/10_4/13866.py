a=list(map(int,input().split()))
a.sort()
b=a[0]+a[3]
c=a[1]+a[2]
print(abs(b-c))