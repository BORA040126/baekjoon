a=int(input())
b=[]
for i in range(a):
    c,d=map(int,input().split())
    b.append([c,d])
b.sort(key=lambda x:x[1])
b.sort(key=lambda x:x[0])
for i in range(len(b)):
    print(b[i][0],b[i][1])