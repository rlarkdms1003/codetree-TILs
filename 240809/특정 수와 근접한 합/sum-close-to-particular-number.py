import itertools

def closest_sum(n, s, nums):
    total_sum = sum(nums)
    min_diff = float('inf')
    
    # 모든 두 숫자의 조합을 탐색
    for a, b in itertools.combinations(nums, 2):
        current_sum = total_sum - (a + b)
        current_diff = abs(s - current_sum)
        min_diff = min(min_diff, current_diff)
    
    return min_diff

# 입력 처리
n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 결과 출력
print(closest_sum(n, s, nums))