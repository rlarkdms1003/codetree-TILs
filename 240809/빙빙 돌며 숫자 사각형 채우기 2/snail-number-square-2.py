n, m = map(int, input().split())

# n * m 크기의 2차원 리스트 초기화
grid = [[0] * m for _ in range(n)]

# 방향을 나타내는 리스트 (아래, 오른쪽, 위쪽, 왼쪽 순)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 초기 시작 위치 및 초기 방향
x, y = 0, 0
direction = 0
num = 1

# 전체 n * m 개의 숫자를 채워나감
for _ in range(n * m):
    grid[x][y] = num
    num += 1

    # 다음 위치 계산
    nx, ny = x + dx[direction], y + dy[direction]

    # 다음 위치가 범위를 벗어나거나 이미 숫자가 채워져 있으면 방향 전환
    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]

    # 다음 위치로 이동
    x, y = nx, ny

# 결과 출력
for row in grid:
    print(" ".join(map(str, row)))