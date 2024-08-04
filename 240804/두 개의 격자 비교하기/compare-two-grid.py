arr1 = tuple(map(int, input().split()))
n = arr1[0]
m = arr1[1]
arr2 = [list(map(int , input().split()))
        for _ in range(n)]
arr3 = [list(map(int ,input().split()))
        for _ in range(m)]
arr4 = [
    [ 0 for _ in range(n)]
    for _ in range(m)
]
for i in range(n):
    for j in range(m):
        if arr2[i][j] == arr3[i][j]:
            arr4[i][j] = 0
        else:
            arr4[i][j] = 1

for i in range(n):
    for j in range(m):
        print(arr4[i][j], end = ' ')
    print()