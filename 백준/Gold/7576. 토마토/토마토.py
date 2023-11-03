from collections import deque

m, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 모든 익은 토마토 위치를 찾아 queue에 추가
q = deque()
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            q.append((i, j))

# BFS 수행
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if array[nx][ny] == 0:
            array[nx][ny] = array[x][y] + 1
            q.append((nx, ny))

# 모든 토마토가 익는데 걸리는 시간 계산
days = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:  # 익지 않은 토마토가 있으면 -1 출력
            print(-1)
            exit(0)
        days = max(days, array[i][j])

# 모든 토마토가 이미 익어있으면 0 출력, 아니면 days - 1 출력
print(0 if days == 1 else days - 1)
