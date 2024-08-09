from datetime import datetime, timedelta

m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

start_date = datetime(2024, m1, d1)
end_date = datetime(2024, m2, d2)

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
target_index = days_of_week.index(target_day)

# start_date의 요일 인덱스 계산 (월요일이 0)
start_day_index = (start_date.weekday() + 1) % 7

# 시작일에서 목표 요일까지 남은 일수 계산
days_to_first_target = (target_index - start_day_index + 7) % 7

# 첫 번째 목표 요일로 이동
first_target_date = start_date + timedelta(days=days_to_first_target)

# 첫 번째 목표 요일이 end_date를 넘는지 확인
if first_target_date > end_date:
    print(0)
else:
    # 두 날짜 사이의 총 일수 계산
    total_days = (end_date - first_target_date).days

    # 목표 요일이 등장하는 횟수 계산
    count = 1 + (total_days // 7)
    print(count)