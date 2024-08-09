def count_cow_combinations(s):
    n = len(s)
    count_c = 0
    count_o = 0
    count_w = 0
    
    for char in s:
        if char == 'C':
            count_c += 1
        elif char == 'O':
            count_o += count_c
        elif char == 'W':
            count_w += count_o
    
    return count_w

# 입력 처리
n = int(input())  # 문자열의 길이 (사용하지 않음)
s = input().strip()

# 결과 출력
print(count_cow_combinations(s))