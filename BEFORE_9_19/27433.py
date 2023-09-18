def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1

a=int(input())
if a==0:
    print("1")
else:
    print(factorial(a))