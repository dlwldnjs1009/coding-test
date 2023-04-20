n = int(input())
data = list(map(int, input().split()))

data_sorted=[i for i in data]
data_sorted.sort()
p = []

for i in data:
    p.append(data_sorted.index(i))
    data_sorted[data_sorted.index(i)] = -1

results = [i for i in p]
for result in results:
    print(result, end=' ')