from itertools import combinations

def no_carry_sum(a, b, c):
    a_str, b_str, c_str = str(a)[::-1], str(b)[::-1], str(c)[::-1]
    max_len = max(len(a_str), len(b_str), len(c_str))
    
    carry = False
    total_sum = 0
    
    for i in range(max_len):
        digit_sum = 0
        if i < len(a_str):
            digit_sum += int(a_str[i])
        if i < len(b_str):
            digit_sum += int(b_str[i])
        if i < len(c_str):
            digit_sum += int(c_str[i])
        
        if digit_sum >= 10:
            carry = True
            break
    
    if carry:
        return -1
    else:
        return a + b + c

def find_max_no_carry_sum(numbers):
    max_sum = -1
    for comb in combinations(numbers, 3):
        current_sum = no_carry_sum(*comb)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# 입력 처리
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 결과 출력
print(find_max_no_carry_sum(numbers))