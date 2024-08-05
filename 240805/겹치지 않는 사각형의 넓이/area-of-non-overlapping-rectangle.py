Ax1, Ay1, Ax2, Ay2 = tuple(map(int ,input().split()))

Bx1, By1, Bx2, By2 = tuple(map(int, input().split()))

Mx1, My1, Mx2, My2 = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(2005)]
    for _ in range(2005)
]

offset = 1000

for y in range(Ay1, Ay2):
    for x in range(Ax1, Ax2):
        arr[y][x] = 1

for y in range(By1, By2):
    for x in range(Bx1, Bx2):
        arr[y][x] = 1

for y in range(My1, My2):
    for x in range(Mx1, Mx2):
        arr[y][x] = 0
ans = 0
for y in range(2005):
    for x in range(2005):
        if arr[y][x] ==1:
            ans +=1
print(ans)