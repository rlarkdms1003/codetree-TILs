class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

Users = []

for _ in range(5):
    name, score = tuple(input().split())
    Users.append(User(name, int(score)))

min = 0
for i in range(1, 5):
    if Users[min].score > Users[i].score:
        min = i

print(Users[min].name, Users[min].score)