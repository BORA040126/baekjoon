a=input()
b=[]
if len(a)>=2:
    c=int(a[0:-1])
    d=int(a[-1])
else:
    c=int(a[0])
    d=int(a[1])
print(c+d)
