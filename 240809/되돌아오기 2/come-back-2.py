commands = input().strip()

# 북, 동, 남, 서 순서로 방향을 나타내는 리스트
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_index = 0  # 처음에는 북쪽을 향하고 있음

x, y = 0, 0

for time, command in enumerate(commands, 1):
    if command == 'L':
        direction_index = (direction_index - 1) % 4
    elif command == 'R':
        direction_index = (direction_index + 1) % 4
    elif command == 'F':
        dx, dy = directions[direction_index]
        x += dx
        y += dy
    
    if x == 0 and y == 0:
        print(time)
        break
else:
    print(-1)