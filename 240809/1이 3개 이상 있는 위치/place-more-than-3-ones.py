n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

ans = 0

def in_range(y,x):
    return 0 <= y < n and 0 <= x <n
for y in range(n):
    for x in range(n):

        yx1cnt = 0

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if in_range(ny,nx) and a[ny][nx] == 1:
                yx1cnt +=1
        
        if yx1cnt >= 3:
            ans += 1

print(ans)