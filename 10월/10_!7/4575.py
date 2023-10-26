while True:
    a = input()
    f = a.replace(" ", "")
    b = []
    if a == "END":
        break
    else:
        for i in f:
            b.append(i)
        
        if len(b) == len(set(b)):
            print(a)

        
