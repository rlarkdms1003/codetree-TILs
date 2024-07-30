arr =list(map(int, input().split()))
cnt = 0
sum = 0
for i in range(10):
    if arr[i] == 0:
        break
    elif arr[i] %2==0:
        cnt +=1
        sum += arr[i]
print(cnt, sum)