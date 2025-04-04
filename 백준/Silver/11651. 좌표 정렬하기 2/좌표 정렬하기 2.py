from sys import stdin

n = int(input())
# sorted함수의 lambda 사용해서 첫번째y로 정렬 후 두번째x로 정렬 하도록
a = []
for _ in range(n):
    b, c = map(int, stdin.readline().split())
    a.append((b,c))

a.sort(key= lambda x : (x[1], x[0]))

for pair in a:
    print(pair[0], pair[1])
