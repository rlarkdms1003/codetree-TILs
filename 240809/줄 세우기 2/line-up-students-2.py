# 입력 받기
n = int(input())
students = []

for i in range(1, n+1):
    h, w = map(int, input().split())
    students.append((h, w, i))

# 키 오름차순, 키가 같으면 몸무게 내림차순으로 정렬
students.sort(key=lambda x: (x[0], -x[1]))

# 결과 출력
for student in students:
    print(student[0], student[1], student[2])