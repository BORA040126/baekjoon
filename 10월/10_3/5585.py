def de(a):
    b = [0, 0, 0, 0, 0, 0]
    b[0] = a // 500
    a = a - b[0] * 500
    b[1] = a // 100
    a = a - b[1] * 100
    b[2] = a // 50
    a = a - b[2] * 50
    b[3] = a//10
    a=a-b[3]*10
    b[4] = a//5
    a=a-b[4]*5
    b[5]=a
    return b


    

c = int(input())
print(sum(de(1000-c)))
