n = int(input())
board = [list(input().strip()) for _ in range(n)]

def check(board):
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1, n):  # 행 검사
            if board[i][j] == board[i][j-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        count = 1
        for j in range(1, n):  # 열 검사
            if board[j][i] == board[j-1][i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
    return max_count

def find_max_candy():
    max_candy = 0
    for i in range(n):
        for j in range(n):
            if j + 1 < n:  # 오른쪽 사탕과 교환
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                max_candy = max(max_candy, check(board))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 원래 상태로 복구
                
            if i + 1 < n:  # 아래 사탕과 교환
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                max_candy = max(max_candy, check(board))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 원래 상태로 복구
                
    return max_candy

print(find_max_candy())
