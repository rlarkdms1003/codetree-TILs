arr = list(map(int, input().split()))
arr2 = []
for i in range(len(arr)):
    if arr[i] == 999 or arr[i]==-999:
        break
    else:
        arr2.append(arr[i])       
print(max(arr2), min(arr2))