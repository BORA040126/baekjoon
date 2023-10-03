import math

a, b, c = map(float, input().split())

height = int((a * b) / math.sqrt(b**2 + c**2))
width = int((a * c) / math.sqrt(b**2 + c**2))

print(height, width)

