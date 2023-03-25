import heapq
n = int(input())
adventurer = list(map(int, input().split()))

count = 0
result = 0
for i in adventurer:
    count += 1
    if count >= i:
        result += 1
        count =0
print(result)