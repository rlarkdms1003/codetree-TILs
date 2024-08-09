n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]

grid = [[0] * 201 for _ in range(201)]

for index, (x1, y1, x2, y2) in enumerate(rectangles):
    color = 1 if index % 2 == 1 else -1
    for i in range(x1 + 100, x2 + 100):
        for j in range(y1 + 100, y2 + 100):
            grid[i][j] = color

blue_area = sum(1 for i in range(201) for j in range(201) if grid[i][j] == 1)

print(blue_area)