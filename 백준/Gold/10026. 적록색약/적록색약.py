import sys

def dfs(r, c, color, is_color_blind):
    if r < 0 or c < 0 or r >= n or c >= n or visited[r][c]:
        return False

    if is_color_blind and color in ['R', 'G']:
        if matrix[r][c] not in ['R', 'G']:
            return False
    elif matrix[r][c] != color:
        return False

    visited[r][c] = True
    dfs(r - 1, c, color, is_color_blind)
    dfs(r, c - 1, color, is_color_blind)
    dfs(r + 1, c, color, is_color_blind)
    dfs(r, c + 1, color, is_color_blind)
    return True

sys.setrecursionlimit(10**6)

n = int(input())
matrix = [list(input()) for _ in range(n)]

normal_result = 0
visited = [[False] * n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            if dfs(r, c, matrix[r][c], False):
                normal_result += 1

color_blind_result = 0
visited = [[False] * n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            if dfs(r, c, matrix[r][c], True):
                color_blind_result += 1

print(normal_result, color_blind_result)
