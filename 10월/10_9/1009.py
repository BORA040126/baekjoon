import sys
a=int(sys.stdin.readline())
b=[10,1,2,3,4,5,6,7,8,9]
for i in range(a):
    c,d=map(int,sys.stdin.readline().split())
    e=(c**d)%10
    print(b[e])
