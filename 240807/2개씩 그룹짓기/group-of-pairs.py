# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))

# 숫자들을 정렬
numbers.sort()

# 그룹의 합 중 최대값을 저장할 변수 초기화
max_group_sum = 0

# 그룹핑: 가장 작은 값과 가장 큰 값을 짝지어서 그룹을 만듦
for i in range(N):
    group_sum = numbers[i] + numbers[2 * N - 1 - i]
    if group_sum > max_group_sum:
        max_group_sum = group_sum

# 결과 출력
print(max_group_sum)