n = int(input())

words = [
    input() for i in range(n)
]

words.sort()

for word in words:
    print(word)