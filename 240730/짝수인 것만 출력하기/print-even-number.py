n = int(input())
arr_new = []
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] %2 == 0:
        arr_new.append(arr[i])
print(*arr_new)