a=input()
b,c=a.split(" ")
d=[]
b=int(b)
c=int(c)

for i in range(1,c+1):
    for j in range(i):
        d.append(i)
print(sum(d[b-1:c]))