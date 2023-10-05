a=list(map(int,input().split()))
b=int(input())
if sum(a)>=b*2:
    print(sum(a)-b*2, end="")
else:
    print(sum(a), end="")