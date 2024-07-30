arr = list(map(int, input().split()))
arr2 = []
for i in range(10):
    if arr[i] == 0:
        break
    else:
        arr2.append(arr[i])
print(*arr2[::-1])