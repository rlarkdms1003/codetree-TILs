# 입력 받기
n, t = map(int, input().split())
commands = input().strip()
grid = [list(map(int, input().split())) for _ in range(n)]

# 초기 설정
x, y = n // 2, n // 2  # 시작 위치
direction = 0  # 초기 방향 (북쪽)
dx = [-1, 0, 1, 0]  # 북, 동, 남, 서 방향의 x 좌표 변화량
dy = [0, 1, 0, -1]  # 북, 동, 남, 서 방향의 y 좌표 변화량

total_sum = grid[x][y]  # 시작 위치의 값 더하기

# 명령 처리
for command in commands:
    if command == 'L':
        direction = (direction - 1) % 4  # 왼쪽 회전
    elif command == 'R':
        direction = (direction + 1) % 4  # 오른쪽 회전
    elif command == 'F':
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n:  # 격자 범위 내에 있을 때만 이동
            x, y = nx, ny
            total_sum += grid[x][y]

# 결과 출력
print(total_sum)