from datetime import datetime

class WeatherForecast:
    def __init__(self, date, weekday, weather):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.weekday = weekday
        self.weather = weather

# 입력 받기
n = int(input())
forecasts = []

for _ in range(n):
    date, weekday, weather = input().split()
    forecasts.append(WeatherForecast(date, weekday, weather))

# 가장 근 시일내에 비가 오는 날 찾기
nearest_rainy_day = None

for forecast in forecasts:
    if forecast.weather == "Rain":
        if nearest_rainy_day is None or forecast.date < nearest_rainy_day.date:
            nearest_rainy_day = forecast

# 결과 출력
if nearest_rainy_day:
    print(f"{nearest_rainy_day.date.strftime('%Y-%m-%d')} {nearest_rainy_day.weekday} {nearest_rainy_day.weather}")