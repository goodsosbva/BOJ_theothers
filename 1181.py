# 1181. 단어 정렬
n = int(input())

words = []
for i in range(n):
    word = input()
    words_len = len(word)
    words.append((word, words_len))

words = set(words)
sorted_word = sorted(words, key= lambda x: (x[1], x[0]))

# print(sorted_word)

for i in range(len(sorted_word)):
    print(sorted_word[i][0])
