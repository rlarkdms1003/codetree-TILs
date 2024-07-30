n = int(input())
arr_new = []
cnt = 1
for i in range(100):
    arr_new.append(n * cnt)
    cnt +=1
    if n * cnt % 11 == 0:
        break
print(*arr_new)