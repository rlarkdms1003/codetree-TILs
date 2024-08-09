n = int(input())

nums = list(map(int, input().split()))

nums.sort()

max_group_sum = 0

for i in range(n):
    group_sum = nums[i] + nums[2*n - 1 - i]
    if group_sum > max_group_sum:
        max_group_sum = group_sum
print(max_group_sum)