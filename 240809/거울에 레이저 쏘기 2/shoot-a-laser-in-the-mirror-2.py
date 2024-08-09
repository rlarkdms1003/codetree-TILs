def simulate_laser(n, grid, start_pos):
    directions = [
        (-1, 0),  # 북
        (0, 1),   # 동
        (1, 0),   # 남
        (0, -1)   # 서
    ]
    
    # 레이저 시작 위치 및 초기 방향 설정
    if start_pos <= n:
        x, y = 0, start_pos - 1
        direction = 2
    elif start_pos <= 2 * n:
        x, y = start_pos - n - 1, n - 1
        direction = 3
    elif start_pos <= 3 * n:
        x, y = n - 1, n - (start_pos - 2 * n)
        direction = 0
    else:
        x, y = 4 * n - start_pos, 0
        direction = 1
    
    reflections = 0
    
    while 0 <= x < n and 0 <= y < n:
        if grid[x][y] == '/':
            direction = [1, 0, 3, 2][direction]
        elif grid[x][y] == '\\':
            direction = [3, 2, 1, 0][direction]
        
        x += directions[direction][0]
        y += directions[direction][1]
        reflections += 1
    
    return reflections

n = int(input())
grid = [input().strip() for _ in range(n)]
k = int(input())

result = simulate_laser(n, grid, k)
print(result)