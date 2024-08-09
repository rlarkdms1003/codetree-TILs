n = int(input())
x, y = 0, 0
for _ in range(n):
    d_str, dist = tuple(input().split())
    dist = int(dist)

    if d_str == 'E':
        x, y = x + dist, y
    elif d_str == 'W':
        x, y = x - dist, y
    elif d_str == 'S':
        x, y = x, y - dist
    else:
        x, y = x, y + dist
print(x, y)