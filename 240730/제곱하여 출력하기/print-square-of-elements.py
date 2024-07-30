n =int(input())
arr = list(map(int, input().split()))
new_arr = []
for elem in arr:
        new_arr.append(elem * elem)
a = int((new_arr[0]))
b = int(new_arr[1])
c = int(new_arr[2])
print(a, b, c)