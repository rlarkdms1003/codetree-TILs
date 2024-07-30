a, b = map(int, input().split())
for i in range(10):
    if i % 2 == 0:
        print(a, end = " ")
        a = b + 2*a
    else:
        print(b, end = " ")
        b = a + 2 * b