a=[]
b=[]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
b.append(int(input()))
b.append(int(input()))

a.sort(reverse=True)
b.sort(reverse=True)
c=a[0]+a[1]+a[2]+b[0]
print(c)