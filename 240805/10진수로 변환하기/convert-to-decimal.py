s = input()
s = list(s)
binary = list(map(int, s))
num = 0

for i in range(len(binary)):
    num = num * 2 + binary[i]

print(num)