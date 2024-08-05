arr = [
    [0 for _ in range(205)]
    for _ in range(205)
]

offset = 100

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for y in range(y1+offset, y2+offset):
        for x in range(x1+offset, x2+offset):
            arr[y][x] +=1

ans = 0
for y in range(0,205):
    for x in range(0, 205):
        if arr[y][x] >= 1:
            ans += 1
print(ans)