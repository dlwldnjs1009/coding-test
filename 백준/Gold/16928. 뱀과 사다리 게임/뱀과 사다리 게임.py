from collections import deque

n, m = map(int, input().split())

graph = [0] * 101
visited = [False] * 101
for i in range(1, 101):
    graph[i] = i

ladder = {}
for i in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

snake = {}
for i in range(m):
    a, b = map(int, input().split())
    snake[a] = b

def bfs():
    q = deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        location, roll_count = q.popleft()

        if location == 100:
            return roll_count

        for i in range(1, 7):
            next_location = location + i

            if next_location > 100:
                continue

            if next_location in ladder:
                next_location = ladder[next_location]

            elif next_location in snake:
                next_location = snake[next_location]

            if  not visited[next_location]:
                visited[next_location] = True
                q.append((next_location, roll_count + 1))

print(bfs())
