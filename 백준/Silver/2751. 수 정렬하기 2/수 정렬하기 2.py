n = int(input())
char = []
for i in range(n):
    char.append(int(input()))

char.sort()
for chars in char:
    print(chars)
