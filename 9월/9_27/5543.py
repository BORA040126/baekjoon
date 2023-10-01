b=[]
d=[]
for i in range(3):
    a=int(input())
    b.append(a)
for i in range(2):
    c=int(input())
    d.append(c)
print(min(b)+min(d)-50)