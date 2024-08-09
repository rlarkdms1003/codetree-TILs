n = int(input())
commands = [input().split() for _ in range(n)]

tiles = {}
position = 0

for x, direction in commands:
    x = int(x)
    
    if direction == "R":
        for i in range(position, position + x):
            if i in tiles:
                tiles[i] = not tiles[i]
            else:
                tiles[i] = True
        position += x - 1
    elif direction == "L":
        for i in range(position, position - x, -1):
            if i in tiles:
                tiles[i] = not tiles[i]
            else:
                tiles[i] = False
        position -= x - 1

white_tiles = sum(1 for v in tiles.values() if not v)
black_tiles = sum(1 for v in tiles.values() if v)

print(white_tiles, black_tiles)