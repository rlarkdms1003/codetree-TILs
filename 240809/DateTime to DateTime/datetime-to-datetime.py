from datetime import datetime

start_time = datetime(2011, 11, 11, 11, 11)
a, b, c = map(int, input().split())
end_time = datetime(2011, 11, a, b, c)

time_difference = end_time - start_time

if time_difference.total_seconds() < 0:
    print(-1)
else:
    print(int(time_difference.total_seconds() // 60))