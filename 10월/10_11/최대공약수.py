a=int(input())
if a==2:
    c=[]
    b,d=map(int,input().split())
 
    while(1):
        f=0
        for i in range(1,min(b,d)+1):
            if b%i==0 and d%i==0:
                c.append(i)
                if i==min(a,b):
                    f=1
                    break
                else:
                    continue
        
        if f==1:
            for j in c:
                print(j)
            break
else:
    c=[]
    b,d,e=map(int,input().split())
    while(1):
        f=0
        for i in range(1,min(b,d,e)+1):
            if b%i==0 and d%i==0 and e%i==0:
                c.append(i)
                if i==min(b,d,e):
                    f=1
                    break
                else:
                    continue
        
        if f==1:
            for j in c:
                print(j)
            break
