from datetime import datetime, timedelta

m1, d1, m2, d2 = map(int, input().split())

start_date = datetime(2011, m1, d1)
target_date = datetime(2011, m2, d2)

day_difference = (target_date - start_date).days
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

result_day = days_of_week[(day_difference % 7)]

print(result_day)