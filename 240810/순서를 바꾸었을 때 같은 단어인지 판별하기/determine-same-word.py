words1 = input().strip()
words2 = input().strip()


if sorted(words1) == sorted(words2):
    print("Yes")
else:
    print("No")