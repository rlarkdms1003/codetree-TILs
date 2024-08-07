n = int(input())
numbers = list(map(int, input().split()))

def find_median(lst):
    sorted_lst = sorted(lst)
    mid = len(sorted_lst) // 2
    return sorted_lst[mid]

current_numbers = []
result = []

for i in range(n):
    current_numbers.append(numbers[i])
    if (i + 1) % 2 != 0:
        result.append(find_median(current_numbers))

print(" ".join(map(str, result)))