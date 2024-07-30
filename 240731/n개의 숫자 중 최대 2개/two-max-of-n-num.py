N = int(input())
arr = list(map(int, input().split()))
if arr[0] > arr[1]:
    max1, max2 = arr[0], arr[1]
else:
    max1, max2 = arr[1], arr[0]
for i in range(2, N):
    if arr[i] >= max1:
        max1, max2 = arr[i], max1
    elif arr[i] > max2:
        max2 = arr[i]
print(max1, max2)