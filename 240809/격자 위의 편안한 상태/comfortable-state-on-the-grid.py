n, m = map(int, input().split())
grid = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    grid[r][c] = 1

    count = 0
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
            count += 1

    if count == 3:
        print(1)
    else:
        print(0)