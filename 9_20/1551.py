num = int(input())
ba = num
a = list(map(int, input().split(",")))

def trans(a):
    b = []
    for i in range(len(a) - 1):
        b.append(a[i] - a[i+1])
    return b

while num > 0:
    a = trans(a)
    num -= 1

for i in range(len(a)):
    if i < len(a) - 1:
        print(a[i], end=",")
    else:
        print(a[i])





    

