def solution(n, computers):
    # 방문 여부 체크 배열 초기화 (0부터 n-1까지의 인덱스 사용)
    visited = [False] * n
    answer = 0

    def dfs(cur_v):
        visited[cur_v] = True
        for next_v in range(n):
            if computers[cur_v][next_v] == 1 and not visited[next_v]:
                dfs(next_v)

    for i in range(n):
        if not visited[i]:  
            dfs(i)
            answer += 1  

    return answer