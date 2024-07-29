arr = list(map(int, input().split()))
sum = 0
cnt=0
for i in range(10):
    if(arr[i]>250):
        break
    sum += arr[i]
    cnt+= 1
print(f"{sum} {sum/cnt:.1f}")