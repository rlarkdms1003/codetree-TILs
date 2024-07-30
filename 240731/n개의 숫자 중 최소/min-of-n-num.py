N = int(input())
arr = list(map(int, input().split()))
min_val = arr[0]
cnt = 0
for elem in arr:
    if min_val > elem:
        min_val = elem
        cnt =1
    elif min_val == elem:
        cnt += 1
print(f"{min_val} {cnt}")