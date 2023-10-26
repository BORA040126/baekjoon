a=list(map(int,input().split()))
a.sort(reverse=True)
if a[0]>=a[1]+a[2]:
    a[0]=a[1]+a[2]-1
    print(sum(a))
else:
    print(sum(a))