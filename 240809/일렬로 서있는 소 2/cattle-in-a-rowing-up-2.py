def count_valid_combinations(n, heights):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if heights[i] <= heights[j] <= heights[k]:
                    count += 1
    return count

# 입력
n = int(input())
heights = list(map(int, input().split()))

# 결과 출력
print(count_valid_combinations(n, heights))