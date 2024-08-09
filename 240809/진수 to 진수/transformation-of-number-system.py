a, b = map(int, input().split())
n = input()

decimal_value = int(n, a)
result = ''

while decimal_value > 0:
    result = str(decimal_value % b) + result
    decimal_value //= b

print(result)