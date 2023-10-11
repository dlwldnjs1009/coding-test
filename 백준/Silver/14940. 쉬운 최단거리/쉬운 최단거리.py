from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
            break

bfs(x, y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1
        print(graph[i][j], end=" ")
    print()
