def pac(a):
    if a<=1:
        return 1
    else:
        return a*pac(a-1)
a=int(input())
print(pac(a)) #재귀 함수 쓰면 안 된다...