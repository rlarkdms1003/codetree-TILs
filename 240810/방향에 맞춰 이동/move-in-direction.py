x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n = int(input())

for _ in range(n):
    d_str, dist = tuple(input().split())
    dist = int(dist)

    if d_str == 'E':
        d_num = 1
    elif d_str == 'W':
        d_num = 3
    elif d_str == 'S':
        d_num = 2
    else:
        d_num = 0
    
    x, y = x + dist * dx[d_num], y + dist * dy[d_num] 
print(x, y)