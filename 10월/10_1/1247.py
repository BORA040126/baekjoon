e=[]
for i in range(3):
    a=int(input())
    b=[]
    for i in range(a):
        d=int(input())
        b.append(d)
    if sum(b)>0:
        e.append("+")
    elif sum(b)==0:
        e.append("0")
    else:
        e.append("-")

for i in range(3):
    print(e[i])
        
