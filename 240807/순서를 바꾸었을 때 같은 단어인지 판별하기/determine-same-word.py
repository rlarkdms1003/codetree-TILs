# 첫 번째 단어 입력 받기
word1 = input().strip()

# 두 번째 단어 입력 받기
word2 = input().strip()

# 두 단어의 문자를 정렬하여 비교
if sorted(word1) == sorted(word2):
    print("Yes")
else:
    print("No")