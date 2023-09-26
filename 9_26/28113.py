a,b,c=map(int,input().split())
if a>c:
    print("Bus")
elif c>b:
    print("Bus")
elif c==b:
    print("Anything")
else:
    print("Subway")