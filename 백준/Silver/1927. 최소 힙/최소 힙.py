import heapq
import sys

input = sys.stdin.readline  # 빠른 입력을 위한 설정
n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(q, x)
    elif x == 0:
        if not q:  # len(q) == 0과 동일
            print(0)
        else:
            print(heapq.heappop(q))
