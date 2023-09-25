i, j = map(int, input().split())
a = (i + j) // 2
b = (i - j) // 2

if (i + j) % 2 == 0 and (i - j) % 2 == 0 and a >= 0 and b >= 0:
    if a > b:
        print(a, b)
    else:
        print(b, a)
else:
    print("-1")
