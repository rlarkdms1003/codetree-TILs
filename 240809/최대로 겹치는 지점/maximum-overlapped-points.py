n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

max_overlap = 0

for point in range(1, 101):
    overlap = 0
    for x1, x2 in segments:
        if x1 <= point <= x2:
            overlap += 1
    max_overlap = max(max_overlap, overlap)

print(max_overlap)