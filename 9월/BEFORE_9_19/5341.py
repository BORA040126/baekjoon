def sum(a):
    if a==1:
        return 1
    else: 
        return a+sum(a-1)
c=[]
while(1):
    b=int(input())
    if b==0:
        break
    else:
        c.append(sum(b))
for i in range(len(c)):
    print(c[i])