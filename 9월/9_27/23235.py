a=0
while(1):
    b=list(map(int,input().split()))
    if b[0]==0 and len(b)==1:
        break
    else:
        a+=1

for i in range(1,a+1):
    print("Case {}: Sorting... done!".format(i))

