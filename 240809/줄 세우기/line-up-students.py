class user:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())
members = []

for i in range(1, n+1):
   h, w = tuple(map(int, input().split()))
   members.append(user(h, w, i))

members.sort(key = lambda x: (-x.height, -x.weight, x.number))

for p in members:
    print(p.height, p.weight, p.number)