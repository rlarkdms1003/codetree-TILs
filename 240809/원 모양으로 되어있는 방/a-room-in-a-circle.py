def calculate_distance(N, people, start):
    total_distance = 0
    for i in range(N):
        distance = (i - start + N) % N
        total_distance += distance * people[i]
    return total_distance

def find_minimum_total_distance(N, people):
    min_distance = float('inf')
    for start in range(N):
        total_distance = calculate_distance(N, people, start)
        if total_distance < min_distance:
            min_distance = total_distance
    return min_distance

# 입력 처리
N = int(input())
people = [int(input()) for _ in range(N)]

# 결과 출력
print(find_minimum_total_distance(N, people))