class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

# n명의 정보를 입력받기
n = int(input())
people = []
for _ in range(n):
    name, height, weight = input().split()
    people.append(Person(name, int(height), int(weight)))

# 키를 기준으로 오름차순, 키가 같으면 몸무게 기준으로 내림차순 정렬
people_sorted = sorted(people, key=lambda p: (p.height, -p.weight))

# 결과 출력
for person in people_sorted:
    print(f"{person.name} {person.height} {person.weight}")