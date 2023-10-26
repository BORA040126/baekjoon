a=int(input())
c=[]
d=[]
b=list(map(str,input().split()))
for i in b:
    c.append(i)

for j in range(len(c)):
    if c[j][-6:]=="Cheese":
        d.append(c[j])
    else:
        continue
d=list(set(d))

if len(d)>=4:
    print("yummy")
else:
    print("sad")
