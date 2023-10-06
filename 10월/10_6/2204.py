while(1):
    a=int(input())
    if a==0:
        break
    else:
        c=[]
        for i in range(a):
            d=input().lower()
            c.append(d)
        c.sort()
        print(c[0])
