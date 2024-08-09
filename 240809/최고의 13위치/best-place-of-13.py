def max_coins_in_1x3_grid(n, grid):
    max_coins = 0
    
    # 격자에서 가능한 모든 1x3 영역을 탐색
    for i in range(n):
        for j in range(n - 2):  # 가로로 3칸을 확인할 수 있는 위치만 탐색
            # 현재 1x3 격자 내의 동전 개수를 계산
            current_coins = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
            # 최대값 갱신
            max_coins = max(max_coins, current_coins)
    
    return max_coins

# 입력 처리
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(max_coins_in_1x3_grid(n, grid))