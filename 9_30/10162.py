a=int(input())
b=0
d=0
e=0
c=a//300
a=a-c*300
b+=c
c=a//60
a=a-c*60
d+=c
c=a//10
a=a-c*10
e+=c
if a==0:
    print(b,d,e)
else:
    print(-1)