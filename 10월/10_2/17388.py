a=list(map(int,input().split()))
if sum(a)>=100:
    print("OK")
elif min(a)==a[0]:
    print("Soongsil")
elif min(a)==a[1]:
    print("Korea")
else:
    print("Hanyang")