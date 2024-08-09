def find_maximum_possible_number(a):
    max_value = 0
    n = len(a)
    
    # 모든 자리수를 순회하며, 한 자리만 바꿔본다
    for i in range(n):
        # 현재 자릿수를 반전
        if a[i] == '0':
            # 0을 1로 바꾸기
            modified = a[:i] + '1' + a[i+1:]
        else:
            # 1을 0으로 바꾸기
            modified = a[:i] + '0' + a[i+1:]
        
        # 2진수를 10진수로 변환하여 최댓값 갱신
        max_value = max(max_value, int(modified, 2))
    
    return max_value

# 입력 처리
a = input().strip()

# 결과 출력
print(find_maximum_possible_number(a))