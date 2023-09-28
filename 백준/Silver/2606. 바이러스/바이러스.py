from collections import deque

com = int(input())
n=int(input())
graph = [[] for _ in range(com+1)]

visited = [False] * (com+1)
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start):
    q = deque([start])
    visited[start] = True
    count = 0
    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                q.append(next_v)
                visited[next_v] = True
                count += 1
    return count
print(bfs(graph, 1))

# count=0
# for i in range(len(visited)):
#     if visited[i] == True:
#         count += 1
# print(count -1)
