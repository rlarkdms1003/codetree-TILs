arr = list(map(float, input().split()))
sum = 0
cnt = 0
for i in range(8):
    sum += float(arr[i])
    cnt+=1
print(f"{sum/cnt:.1f}")