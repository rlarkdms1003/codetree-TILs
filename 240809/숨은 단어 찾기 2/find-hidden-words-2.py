def count_lee_in_grid(grid, n, m):
    count = 0
    target = "LEE"
    length = len(target)
    
    directions = [
        (0, 1),  # 가로 (오른쪽)
        (1, 0),  # 세로 (아래쪽)
        (1, 1),  # 대각선 (우하단)
        (1, -1)  # 대각선 (좌하단)
    ]
    
    for i in range(n):
        for j in range(m):
            for dx, dy in directions:
                found = True
                for k in range(length):
                    ni = i + k * dx
                    nj = j + k * dy
                    if ni < 0 or ni >= n or nj < 0 or nj >= m or grid[ni][nj] != target[k]:
                        found = False
                        break
                if found:
                    count += 1
    
    return count

# 입력 처리
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# 결과 출력
print(count_lee_in_grid(grid, n, m))