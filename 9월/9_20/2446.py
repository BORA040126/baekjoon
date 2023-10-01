a=int(input())
for i in range(a,1,-1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1))
