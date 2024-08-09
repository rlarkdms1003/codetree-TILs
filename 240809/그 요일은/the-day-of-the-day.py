from datetime import datetime, timedelta

m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

start_date = datetime(2024, m1, d1)
end_date = datetime(2024, m2, d2)

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

target_index = days_of_week.index(target_day)

count = 0
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() == target_index:
        count += 1
    current_date += timedelta(days=1)

print(count)