def cal_minutes(h, m):
    return 60*h+m

a, b, c, d = tuple(map(int, input().split()))
print(cal_minutes(c, d) - cal_minutes(a, b))