import heapq

n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count = 0
max_distance = 0
for d in distance:
    if d!= INF:
        count +=1
        max_distance = max(max_distance, d)

# 시작 노드 제외해야 하므로 count -1
print(count-1, max_distance)


