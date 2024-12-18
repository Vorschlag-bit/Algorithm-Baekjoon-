import sys

def sort_words(words):
    sorted_words = dict(sorted(words.items(), key=lambda x: (x[1], x[0])))
    return sorted_words

N = int(sys.stdin.readline())
words = {}
for _ in range(N):
    word = sys.stdin.readline().strip()
    words[word] = len(word)

sorted_words = sort_words(words)
for word in sorted_words:
    print(word)