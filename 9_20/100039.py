def switch(a):
    if a<40:
        return 40
    else:
        return a



a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=(switch(a)+switch(b)+switch(c)+switch(d)+switch(e))//5
print(f)
