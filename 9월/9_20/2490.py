for i in range(3):
    yut = list(map(int, input().split()))

    num_backs = yut.count(0)

    num_fronts = yut.count(1)

    if num_backs == 0:  
        print("E")
    elif num_backs == 1:  
        print("A")
    elif num_backs == 2:  
        print("B")
    elif num_backs: 
        print("C")
    else:
        print("D")
    