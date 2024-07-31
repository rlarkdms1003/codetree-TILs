class person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight =  weight

n = int(input())
members = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    members.append(person(name, int(height), int(weight)))

members.sort(key= lambda x : x.height)

for p in members:
    print(f"{p.name} {p.height} {p.weight}")