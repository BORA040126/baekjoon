a=list(map(int,input().split(" ")))
i=0
while(1):
    try:
        if a[i]==1 or a[i]==0:
            i+=1
        else:
            print("F")
            break
    except:
        print("S")
        break