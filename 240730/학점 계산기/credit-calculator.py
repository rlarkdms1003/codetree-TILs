n = int(input())
m = list(map(float, input().split()))
print(f"{sum(m)/n:.1f}")
if sum(m)/n >= 4.0:
    print("Perfect")
elif sum(m)/n >= 3.0:
    print("Good")
else:
    print("Poor")