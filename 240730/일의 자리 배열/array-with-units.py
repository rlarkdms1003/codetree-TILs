a, b = tuple(map(int, input().split()))
arr = []
arr.append(a)
arr.append(b)
for i in range(2, 10):
    arr.append((arr[i-2]+ arr[i-1]) % 10)

print(*arr)