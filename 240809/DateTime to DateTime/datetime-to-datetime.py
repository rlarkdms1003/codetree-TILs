from datetime import datetime

# 기준 날짜와 시간
start_time = datetime(2011, 11, 11, 11, 11)

# 입력 받기
a, b, c = map(int, input().split())

# 입력된 날짜와 시간을 기반으로 새로운 datetime 객체 생성
end_time = datetime(2011, 11, a, b, c)

# 시간 차이 계산
time_difference = end_time - start_time

# 만약 end_time이 start_time보다 앞선다면
if time_difference.total_seconds() < 0:
    print(-1)
else:
    # 분 단위로 출력
    print(time_difference.total_seconds() // 60)