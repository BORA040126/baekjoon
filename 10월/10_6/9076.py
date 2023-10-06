a=int(input())
for i in range(a):
    b=list(map(int,input().split()))
    b.sort()
    c=b[1:-1]
    if c[-1]-c[0]>=4:
        print("KIN")
    else:
        print(sum(c))