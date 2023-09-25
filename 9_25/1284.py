b = []

while True:
    a = input()
    c = 0
    if int(a) == 0:
        break
    for i in range(len(a)):
        if int(a[i]) == 1:
            c += 2
        elif int(a[i]) == 0:
            c += 4
        else:
            c += 3
    weight = c + 2+len(a)-1
    b.append(weight)

for weight in b:
    print(weight)

    
