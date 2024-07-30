n = int(input())
arr = list(map(int, input().split()))

max_arr = -1

for curr_num in arr:
    if max_arr < curr_num:
        count = 0
        for elem in arr:
            if elem == curr_num:
                count += 1
        
        if count == 1:
            max_arr == curr_num
print(max_arr)