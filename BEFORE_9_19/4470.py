a=int(input())
b=[]
for i in range(a):
    c=input()
    b.append(c)

for i in range(1,a+1):
    print(str(i)+". "+b[i-1])