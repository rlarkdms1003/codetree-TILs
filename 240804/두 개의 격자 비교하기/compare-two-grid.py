n, m = (map(int, input().split()))
arr2 = [list(map(int , input().split()))
        for _ in range(n)]
arr3 = [list(map(int ,input().split()))
        for _ in range(n)]
arr4 = [
    [ 0 for _ in range(m)]
    for _ in range(n)
]
for i in range(n):
    for j in range(m):
        if arr2[i][j] == arr3[i][j]:
            arr4[i][j] = 0
        else:
            arr4[i][j] = 1

for row in arr4:
    for elem in row:
        print(elem, end = ' ')
    print()