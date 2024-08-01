arr = list(map(int, input().split()))
max_below_500 = -1
min_above_500 = 1001
for num in arr:
    if num < 500 and num > max_below_500:
        max_below_500  = num
    if num > 500 and num < min_above_500:
        min_above_500 = num
print(max_below_500, min_above_500)