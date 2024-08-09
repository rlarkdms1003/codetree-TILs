def count_valid_pairs(A):
    count = 0
    n = len(A)
    
    for i in range(n - 3):  # n-3까지 탐색하는 이유는 i+3까지 볼 필요가 있기 때문
        if A[i] == '(' and A[i+1] == '(':  # 여는 괄호 쌍을 찾음
            for j in range(i + 2, n - 1):  # 닫는 괄호 쌍을 찾음
                if A[j] == ')' and A[j+1] == ')':
                    count += 1
                    
    return count

# 입력 처리
A = input().strip()

# 결과 출력
print(count_valid_pairs(A))