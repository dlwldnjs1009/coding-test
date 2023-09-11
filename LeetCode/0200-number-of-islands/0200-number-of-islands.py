from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def isValid(r, c):
            return 0 <= r < len(grid) and 0<= c < len(grid[0]) and grid[r][c] == '1'

        def dfs(r, c):
            visited[r][c] = True
            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]
            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]
                if isValid(next_r, next_c):
                    if not visited[next_r][next_c]:
                        dfs(next_r, next_c)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    result += 1

        return result


