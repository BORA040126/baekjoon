while(1):
    a=int(input())
    b=[]
    if a==-1:
        break
    else:
        for i in range(1,a):
            if a%i==0:
                b.append(i)
        if(sum(b)==a):
            print(a,end=" ")
            print("=",end=" ")
            for j in range(0,len(b)):
                if j==(len(b)-1):
                    print(b[j])
                else:
                    print(b[j],end=" ")
                    print("+",end=" ")
        else:
            print(a,end=" ")
            print("is NOT perfect.")




