n = int(input())
arr = list(map(int, input().split()))
max_profit = 0
min_price = float('inf')

for price in arr:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
print(max_profit)