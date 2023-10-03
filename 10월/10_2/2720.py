def de(a):
    b = [0, 0, 0, 0]
    b[0] = a // 25
    a = a - b[0] * 25
    b[1] = a // 10
    a = a - b[1] * 10
    b[2] = a // 5
    a = a - b[2] * 5
    b[3] = a
    print("{} {} {} {}".format(b[0], b[1], b[2], b[3]))

c = int(input())
for i in range(c):
    de(int(input()))
