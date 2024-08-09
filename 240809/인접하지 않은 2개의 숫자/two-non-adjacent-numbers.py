def max_non_adjacent_sum(numbers):
    n = len(numbers)
    max_sum = 0

    for i in range(n):
        for j in range(i + 2, n):  # 인접하지 않은 숫자만 고려 (i+2부터 시작)
            current_sum = numbers[i] + numbers[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
print(max_non_adjacent_sum(numbers))