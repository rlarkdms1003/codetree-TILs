n = int(input())
arr = list(map(int, input().split()))
while True:
    max1 =0
    for i in range(1, n):
        if arr[i] > arr[max1]:
            max1 = i

    print(max1 + 1, end = " ")

    if max1 == 0:
        break
    
    n = max1