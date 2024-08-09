n = int(input())
position = 0
visited = {}

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    
    if direction == 'R':
        for i in range(position + 1, position + x + 1):
            if i in visited:
                visited[i] += 1
            else:
                visited[i] = 1
        position += x
    elif direction == 'L':
        for i in range(position - 1, position - x - 1, -1):
            if i in visited:
                visited[i] += 1
            else:
                visited[i] = 1
        position -= x

overlap_count = sum(1 for count in visited.values() if count > 1)

print(overlap_count)