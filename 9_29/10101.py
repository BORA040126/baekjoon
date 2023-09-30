a=[]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
if sum(a)!=180:
    print("Error")
elif len(list(set(a)))==2:
    print("Isosceles")
elif len(list(set(a)))==1:
    print("Equilateral")
else:
    print("Scalene")

