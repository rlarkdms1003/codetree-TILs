arr = list(map(int, input().split()))
arr2 = []
for i in range(len(arr)):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        arr2.append(int(arr[i]/2))
    else:
        arr2.append(arr[i]+3)
print(*arr2)