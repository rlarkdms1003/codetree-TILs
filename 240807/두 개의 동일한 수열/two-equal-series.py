# 입력 받기
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 수열 정렬
A.sort()
B.sort()

# 비교하여 결과 출력
if A == B:
    print("Yes")
else:
    print("No")