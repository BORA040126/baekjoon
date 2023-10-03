a=int(input())
b=[]
for i in range(a):
    c,d=map(int, input().split())
    e=2-c+d
    b.append(e)

for j in range(len(b)):
    print(b[j])