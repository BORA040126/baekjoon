a=int(input())
b=str(a)

if ("7" not in b) and a%7!=0:
    print(0)
elif ("7" not in b) and a%7==0:
    print(1)
elif ("7" in b) and a%7!=0:
    print(2)
else:
    print(3)