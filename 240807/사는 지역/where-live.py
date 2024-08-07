class Person:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

# 입력 받기
n = int(input())
people = []

for _ in range(n):
    name, address, city = input().split()
    people.append(Person(name, address, city))

# 이름이 사전순으로 가장 느린 사람 찾기
person_with_latest_name = max(people, key=lambda person: person.name)

# 결과 출력
print(f"name {person_with_latest_name.name}")
print(f"addr {person_with_latest_name.address}")
print(f"city {person_with_latest_name.city}")