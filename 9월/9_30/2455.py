max=0
people=0
for i in range(4):
    a,b=map(int,input().split())
    people=people-a+b
    if people>max:
        max=people

print(max)
