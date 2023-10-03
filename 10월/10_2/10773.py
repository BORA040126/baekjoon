c=int(input())
b=[]
for i in range(c):
    a=int(input())
    if a==0:
        b.pop()
    else:
        b.append(a)
print(sum(b))
