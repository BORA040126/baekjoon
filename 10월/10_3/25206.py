def score(a,b):
    a=float(a)
    c=0
    if b=="A+":
        return (4.5*a)
    elif b=="A0":
        return (4.0*a)
    elif b=="B+":
        return (3.5*a)
    elif b=="B0":
        return (3.0*a)
    elif b=="C+":
        return (2.5*a)
    elif b=="C0":
        return (2.0*a)
    elif b=="D+":
        return (1.5*a)
    elif b=="D0":
        return (1.0*a)
    elif b=="F":
        return (0*a)
    else:
        return 0
    

c=[]
e=0
for i in range(10):
    b=list(map(str,input().split()))
    c.append(score(b[1],b[2]))
    if b[2]=="P":
        continue
    else:
        e+=1
        
print(sum(c)/e)