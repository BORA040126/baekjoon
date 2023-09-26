a=input()
b=[]
for i in a:
    b.append(i)
c=len(b)-len(set(b))
print(c)