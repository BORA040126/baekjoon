a = []
b = int(input())
for i in range(b):
    c, d = input().split()
    a.append((int(c), d, i))

a = sorted(a, key=lambda x: (x[0], x[2]))

for c, d, _ in a:
    print(c, d)





