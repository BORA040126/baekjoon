c = 1

while True:
    a = input()
    b = input()

    if a == "END":
        break

    d = list(a)
    e = list(b)

    d.sort()
    e.sort()

    if d == e:
        print("Case {}: same".format(c))
    else:
        print("Case {}: different".format(c))

    c += 1
