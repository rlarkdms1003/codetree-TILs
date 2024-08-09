# 입력 받기
n = int(input())
points = []

# 각 점의 위치와 인덱스를 리스트에 저장
for i in range(n):
    x, y = map(int, input().split())
    distance = abs(x) + abs(y)
    points.append((distance, i + 1))

# 거리 순으로, 거리가 같으면 인덱스 순으로 정렬
points.sort(key=lambda p: (p[0], p[1]))

# 결과 출력
for point in points:
    print(point[1])