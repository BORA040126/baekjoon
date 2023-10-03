a, b = map(int, input().split())
fish_shapes = []
for _ in range(a):
    line = input()
    fish_shapes.append(line)
for i in range(a):
    reversed_shape = fish_shapes[i][::-1]
    print(reversed_shape)
