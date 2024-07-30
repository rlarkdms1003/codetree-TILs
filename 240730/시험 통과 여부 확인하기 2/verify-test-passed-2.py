n = int(input())
arr2 = []
cnt = 0
for i in range(n):
    arr = list(map(int, input().split()))
    sum_val = sum(arr)
    if sum_val/4 >= 60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(f"{cnt}")