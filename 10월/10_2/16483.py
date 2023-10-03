a=input()
b=[]
for i in a:
    b.append(i)

b.sort()
d=""
for j in range(len(b)):
    d=b[j]+d

print(d)

    