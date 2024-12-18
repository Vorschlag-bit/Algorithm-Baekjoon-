def sort_word(word):
    return len(word), word

n = int(input())  # 단어를 입력받을 단어의 개수
words = []  # 단어를 입력받을 배열

# n개의 단어 입력받기
for _ in range(n):
    words.append(input())


# 중복 제거를 위한 set 반환 후,
# sort_word 함수를 사용해 정렬
sorted_words = sorted(list(set(words)), key=sort_word)

for word in sorted_words:
    print(word)

