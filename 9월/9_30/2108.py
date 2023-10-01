import math
a=int(input())
b=[]
c={}
for i in range(a):
    num=int(input())
    b.append(num)
b.sort()
e=sum(b)/a

print(round(e))
print(b[a//2])

for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
sorted_items = sorted(c.items(), key=lambda x: x[0])
sorted_items = sorted(sorted_items, key=lambda x: x[1], reverse=True)

max_frequency = sorted_items[0][1]
if len(sorted_items) > 1 and sorted_items[1][1] == max_frequency:
    print(sorted_items[1][0])
else:
    print(sorted_items[0][0])

print(b[-1]-b[0])




    








