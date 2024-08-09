n, t = tuple(map(int, input().split()))
r,c, d_Str = tuple(input().split())
r,c = int(r), int(c)

dc, dr = [1, 0, 0, -1], [0, -1, 1, 0]
mapper = {
    'U': 1,
    'D': 2,
    'R': 0,
    'L': 3,
}
d = mapper[d_Str]

def in_range(y, x):
    return 1 <= y <= n and 1 <= x <= n

for _ in range(t):
    nr, nc = r + dr[d], c + dc[d]

    if not in_range(nr, nc):
        d = 3 - d 
    else:
        r, c = nr, nc

print(r, c)