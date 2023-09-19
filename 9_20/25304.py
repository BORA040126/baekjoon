a=int(input())
b=int(input())
c=0
for i in range(b):
    d=input()
    e,f=d.split(" ")
    d=int(e)
    f=int(f)
    c+=(d*f)

if c==a:
    print("Yes")
else:
    print("No")
