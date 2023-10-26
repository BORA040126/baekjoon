a,b=map(int,input().split())
dic={}
for i in range(a):
    c,d=input().split()
    dic[c]=d

for j in range(b):
    print(dic.get(input()))

