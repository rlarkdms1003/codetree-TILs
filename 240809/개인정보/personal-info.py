class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

# 5명의 정보를 입력받기
people = []
for _ in range(5):
    name, height, weight = input().split()
    people.append(Person(name, int(height), float(weight)))

# 이름순으로 정렬하여 출력
people_sorted_by_name = sorted(people, key=lambda p: p.name)
print("name")
for person in people_sorted_by_name:
    print(f"{person.name} {person.height} {person.weight:.1f}")

# 키가 큰 순으로 정렬하여 출력
people_sorted_by_height = sorted(people, key=lambda p: p.height, reverse=True)
print("\nheight")
for person in people_sorted_by_height:
    print(f"{person.name} {person.height} {person.weight:.1f}")