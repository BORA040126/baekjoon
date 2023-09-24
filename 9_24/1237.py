import sys
while(1):
    a=int(sys.stdin.readline())
    d=0
    e=[]
    for i in range(a):
        c=int(sys.stdin.readline())
        d+=c
    
    if d==0:
        e.append("0")
    elif d>0:
        e.append("+")
    else:
        e.append("-")
for i in range(len(e)):
    print(e[i])

