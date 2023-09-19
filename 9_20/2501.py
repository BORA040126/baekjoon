a=input()
b,c=a.split(" ")
b=int(b)
c=int(c)
d=[]
for i in range(1,b+1):
    if b%i==0:
        d.append(i)
try:
    print(d[c-1])
except:
    print("0")
