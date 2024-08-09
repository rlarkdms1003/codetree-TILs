n = int(input())

class user:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

users = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    users.append(user(name, int(height), int(weight)))

users.sort(key = lambda x: x.height)

for user in users:
    print(user.name, user.height, user.weight)