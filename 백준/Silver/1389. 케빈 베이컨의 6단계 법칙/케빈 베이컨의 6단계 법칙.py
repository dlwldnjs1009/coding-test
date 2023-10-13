INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = [0] * (n+1)

# 케빈 베이컨 수 계산
result = [0] * (n+1)
for a in range(1, n+1):
    result[a] = sum(graph[a])

# 케빈 베이컨 수가 가장 작은 사람 찾기
print(result.index(min(result[1:])))

