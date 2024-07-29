arr = input().split()
#i => 9 8 7 6 .. 3 2 1 0
for item in arr[::-1]:
    print(item, end='')