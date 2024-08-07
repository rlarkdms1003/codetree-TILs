# 입력 받기
n, k, T = input().split()
n = int(n)
k = int(k)

words = [input().strip() for _ in range(n)]

# 문자열 T로 시작하는 단어들 필터링
filtered_words = [word for word in words if word.startswith(T)]

# 사전순으로 정렬
filtered_words.sort()

# k번째 단어 출력 (1-based index이므로 k-1)
print(filtered_words[k - 1])