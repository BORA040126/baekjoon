a=[]
for i in range(10):
    a.append(int(input()))
b=[]
for j in range(10):
    b.append(int(input()))

a.sort(reverse=True)
b.sort(reverse=True)
d=a[0]+a[1]+a[2]
e=b[0]+b[1]+b[2]
print(str(d),str(e))