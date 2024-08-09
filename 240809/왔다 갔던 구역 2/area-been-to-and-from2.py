n = int(input())
commands = [input().split() for _ in range(n)]

visited = set()
overlapped = set()
position = 0

for x, direction in commands:
    x = int(x)
    if direction == "R":
        for i in range(position + 1, position + x + 1):
            if i in visited:
                overlapped.add(i)
            visited.add(i)
        position += x
    elif direction == "L":
        for i in range(position - 1, position - x - 1, -1):
            if i in visited:
                overlapped.add(i)
            visited.add(i)
        position -= x

print(len(overlapped))