a=int(input())
c=[]
for i in range(a):
    b=list(map(int,input().split()))
    d=b.copy()
    b.sort()
    if (d[1]==b[1] and d[0]==b[0]) or (d[0]==b[2] and d[1]==b[1]):
        c.append("Ordered")
    else:
        c.append("Unordered")

print("Gnomes:")
for i in c:
    print(i)
        