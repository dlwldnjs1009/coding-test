n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# b의 최댓값들을 a의 최솟값과 곱해야 함.
# 어떻게 곱할까?
# b의 최댓값 인덱스를 알아야 함
# a의 최솟값 인덱스


sum = 0
for i in range(n):
    sum += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
print(sum)

