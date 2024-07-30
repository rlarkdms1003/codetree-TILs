arr = list(map(int, input().split()))
arr2 = []
for i in range(10):
    if arr[i] % 2 == 0:
        arr2.append(int(arr[i]/2))
    elif arr[i] == 0:
        break
    else:
        arr2.append(arr[i]+3)
print(*arr2)