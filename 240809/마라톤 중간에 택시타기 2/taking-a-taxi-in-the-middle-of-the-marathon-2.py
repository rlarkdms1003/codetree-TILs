def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def minimum_marathon_distance(n, checkpoints):
    # 기본 경로 계산 (모든 체크포인트를 거치는 경우)
    total_distance = 0
    for i in range(1, n):
        total_distance += manhattan_distance(checkpoints[i - 1], checkpoints[i])
    
    min_distance = total_distance
    
    # 한 개의 체크포인트를 건너뛰는 경우 계산
    for i in range(1, n - 1):
        # i번째 체크포인트를 건너뛴 경우의 거리
        skipped_distance = total_distance
        skipped_distance -= manhattan_distance(checkpoints[i - 1], checkpoints[i])
        skipped_distance -= manhattan_distance(checkpoints[i], checkpoints[i + 1])
        skipped_distance += manhattan_distance(checkpoints[i - 1], checkpoints[i + 1])
        
        # 최소 거리 갱신
        min_distance = min(min_distance, skipped_distance)
    
    return min_distance

# 입력 처리
n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(minimum_marathon_distance(n, checkpoints))