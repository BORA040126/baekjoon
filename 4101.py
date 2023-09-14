while(1):
    num=input()
    a,b=num.split(" ")
    a=int(a)
    b=int(b)
    if(a==0&b==0):
       break
    if a>b:
     print("Yes")
    else:
        print("No")