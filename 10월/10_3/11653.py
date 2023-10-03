a=int(input())
b=[]
while(a>1):
    for i in range(2,a+1):
        if a%i==0:
            b.append(i)
            a=a//i
            break

for i in b:
    print(i)
            
