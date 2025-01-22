import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
num_arr = list(map(int, input().split()))

card_counts = Counter(num_arr)

m = int(input())
query_nums = list(map(int, input().split()))

result = []
for num in query_nums:
    result.append(str(card_counts[num]))

print(' '.join(result))
