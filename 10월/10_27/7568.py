a=int(input())
d=[]
for i in range(a):
    b,c=map(int,input().split())
    d.append((b,c))

for i in d:
    rank = 1
    for j in d:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")



