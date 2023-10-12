import itertools
a=[]
for i in range(9):
    a.append(int(input()))
for i in itertools.combinations(a, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break

