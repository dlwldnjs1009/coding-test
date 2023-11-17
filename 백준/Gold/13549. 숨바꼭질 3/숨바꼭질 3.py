from collections import deque

def bfs(n, k):
    if n >= k:
        return n - k

    visited = [False] * 100001
    q = deque([(n, 0)])
    visited[n] = True

    while q:
        current, time = q.popleft()

        if current == k:
            return time

        if 0 <= current * 2 <= 100000 and not visited[current * 2]:
            q.appendleft((current * 2, time))  
            visited[current * 2] = True

        for next_step in (current - 1, current + 1):
            if 0 <= next_step <= 100000 and not visited[next_step]:
                q.append((next_step, time + 1))
                visited[next_step] = True

n, k = map(int, input().split())
print(bfs(n, k))
