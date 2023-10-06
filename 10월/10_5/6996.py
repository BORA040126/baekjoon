a=int(input())
b=[]
for i in range(a):
    c=list(map(str,input().split()))
    d=sorted(c[0])
    f=sorted(c[1])
    if d==f:
        print('{} & {} are anagrams'.format(c[0],c[1]))
    else:
        print('{} & {} are NOT anagrams'.format(c[0],c[1]))