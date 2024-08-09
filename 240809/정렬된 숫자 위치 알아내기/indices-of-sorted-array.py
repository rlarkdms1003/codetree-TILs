# 입력 받기
n = int(input())
sequence = list(map(int, input().split()))

# 원래 위치와 함께 수열을 저장
indexed_sequence = [(value, index) for index, value in enumerate(sequence)]

# 수열을 값 기준으로 정렬
sorted_sequence = sorted(indexed_sequence, key=lambda x: x[0])

# 원래 위치에서 정렬된 위치로 매핑
result = [0] * n
for sorted_index, (value, original_index) in enumerate(sorted_sequence):
    result[original_index] = sorted_index + 1  # 1-based index

# 결과 출력
print(" ".join(map(str, result)))