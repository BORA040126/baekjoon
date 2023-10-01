a=int(input())
b=[1,1]
for i in range(2,a):
    b.append(b[-1]+b[-2])
print(b[-1])
        
