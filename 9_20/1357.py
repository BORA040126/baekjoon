def rev(a):
    b=""
    for i in range(len(a)):
        b=a[i]+b
    return b

a=input()
b,c=a.split(" ")
d=rev(b)
e=rev(c)
d=int(d)
e=int(e)
f=d+e
f=rev(str(f))
f=int(f)
print(f)