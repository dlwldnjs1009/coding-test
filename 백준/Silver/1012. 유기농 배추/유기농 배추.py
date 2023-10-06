from collections import deque

def bfs(graph, start_x, start_y, visited):
    result = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * (m) for _ in range(n)]
    visited = [[False] * (m) for _ in range(n)]
    for j in range(k):
        b,a = map(int, input().split())
        graph[a][b] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(graph, i, j, visited)
                count += 1
    print(count)
