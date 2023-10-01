c=[]
while(1):
    try:
        a, b = map(int, input().split())
        c.append(b//(a+1))
    except:
        for i in range(len(c)):
            print(c[i])
        break

