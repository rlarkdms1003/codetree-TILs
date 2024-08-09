# 입력 받기
N, B = map(int, input().split())

# 진수 변환
if B == 4:
    result = format(N, 'o')  # 'o'는 8진수를 나타냄, 4진수는 수동으로 계산
    result_in_base_4 = ""
    while N > 0:
        result_in_base_4 = str(N % 4) + result_in_base_4
        N = N // 4
    print(result_in_base_4)
elif B == 8:
    result = format(N, 'o')  # 'o'는 8진수를 나타냄
    print(result)