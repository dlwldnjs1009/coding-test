from sys import stdin

words = []
n = int(input())
for i in range(n):
    words.append(stdin.readline().rstrip())

words_set = set(words)
words = list(words_set)

words.sort()
words.sort(key=len)

for j in range(len(words)):
    print(words[j])
