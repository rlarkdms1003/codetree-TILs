class spy:
    def __init__(self, name, score):
        self.name = name
        self.score = score

spies = []
for _ in range(5):
    name, score = tuple(input().split())
    spies.append(spy(name, int(score)))

min = 0

for i in range(1,5):
    if spies[min].score > spies[i].score:
        min = i

print(spies[min].name, spies[min].score)