a = int(input())
b = int(input())
c = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(a, b + 1):
    if is_prime(num):
        c.append(num)

if len(c) == 0:
    print(-1)
else:
    prime_sum = sum(c)
    print(prime_sum)
    print(c[0])  
