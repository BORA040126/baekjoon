def pel(a):
    while(1):
        if len(a)<=1:
            return "yes"
        elif(a[0]==a[-1]):
            return pel(a[1:-1])
        else:
            return "no"

b=[]       
while(1):
    a=input()
    if a=="0":
        break
    b.append(pel(a))

for i in range(len(b)):
    print(b[i])


