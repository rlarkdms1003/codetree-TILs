cmd_list = input()
x, y = 0,0
dir_num = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for cmd in cmd_list:

    if cmd == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]
print(x, y)