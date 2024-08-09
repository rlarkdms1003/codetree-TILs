n, m = map(int, input().split())

# n * m 크기의 2차원 리스트 초기화
grid = [[''] * m for _ in range(n)]

# 방향을 나타내는 리스트 (오른쪽, 아래, 왼쪽, 위 순)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 시작 위치 및 초기 방향
x, y = 0, 0
direction = 0
current_char = 'A'

# 전체 n * m 개의 알파벳을 채워나감
for _ in range(n * m):
    grid[x][y] = current_char
    
    # 다음 알파벳으로 이동 (Z 다음에는 다시 A)
    if current_char == 'Z':
        current_char = 'A'
    else:
        current_char = chr(ord(current_char) + 1)

    # 다음 위치 계산
    nx, ny = x + dx[direction], y + dy[direction]

    # 다음 위치가 범위를 벗어나거나 이미 채워져 있으면 방향 전환
    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != '':
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]

    # 다음 위치로 이동
    x, y = nx, ny

# 결과 출력
for row in grid:
    print(" ".join(row))