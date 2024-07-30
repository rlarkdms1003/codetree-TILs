n = int(input())
arr_new = []
cnt = 1
cmt = 0
for i in range(100):
    arr_new.append(n * cnt)
    if n * cnt % 5 == 0:
        cmt +=1
        if cmt ==2:
            break
    cnt += 1
print(*arr_new)