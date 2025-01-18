import sys

n = int(sys.stdin.readline())
integer = list(map(int, input().split()))
dict = {}
for i in integer:
    dict[i] = 0

for ints in integer:
    dict[ints] = 1

m = int(sys.stdin.readline())
ans = list(map(int, input().split()))

# ans를 integer에서 가지고 있으면 1 출력, 아니면 0 출력, 구분자 = 공백
for an in ans:
    if an in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
