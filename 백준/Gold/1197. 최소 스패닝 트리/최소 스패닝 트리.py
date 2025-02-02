import sys
import heapq

def main():
    input = sys.stdin.readline
    v, e = map(int, input().split())

    # 인접 리스트 구성 (정점 번호 1부터 사용)
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, cost = map(int, input().split())
        adj[a].append((cost, b))
        adj[b].append((cost, a))

    visited = [False] * (v + 1)  # 각 정점이 MST에 포함되었는지 여부
    cnt = 0  # 선택된 간선의 수

    # 최소 힙(우선순위 큐): (비용, 정점1, 정점2)
    pq = []
    
    # MST 전체 비용을 누적할 변수
    mst_cost = 0

    # 시작 정점 1 선택
    visited[1] = True
    for cost, nxt in adj[1]:
        heapq.heappush(pq, (cost, 1, nxt))

    # MST 간선 수는 (정점 수 - 1)개가 될 때까지 반복
    while cnt < v - 1 and pq:
        cost, a, b = heapq.heappop(pq)
        if visited[b]:
            continue

        # MST에 포함되는 간선 비용을 누적
        mst_cost += cost
        
        visited[b] = True
        cnt += 1
        for next_cost, next_vertex in adj[b]:
            if not visited[next_vertex]:
                heapq.heappush(pq, (next_cost, b, next_vertex))

    # MST 비용 출력
    print(mst_cost)

if __name__ == "__main__":
    main()
