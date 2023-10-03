while(1):
    a=list(map(int,input().split()))
    a.sort()
    b=sum(a)
    c=set(a)
    if b==0:
        break
    elif a[0]+a[1]<=a[2]:
        print("Invalid")
    elif len(c)==3:
        print("Scalene")
    elif len(c)==2:
        print("Isosceles")
    else:
        print("Equilateral")
