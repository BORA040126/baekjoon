count=0
a=int(input())
while(a==1):
    if a%6==0:
        a=a/3
        count=count+1
    elif a%3==0:
        a=a/3
        count=count+1
    elif a%2==0:
        a=a/2
        count=count+1
    else:
        a=a-1
        count=count+1

print(count)
