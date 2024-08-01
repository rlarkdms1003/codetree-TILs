n = 4
#for _ in range(n):
    #arr = list(map(int, input().split()))
    #print(sum(arr))
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]
n = 4
for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += arr_2d[j][i]
    print(sum_val)