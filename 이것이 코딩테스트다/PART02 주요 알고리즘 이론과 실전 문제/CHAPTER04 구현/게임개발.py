n, m = map(int, input().split())
#방문한 위치 저장 리스트
d = [[0]*m for _ in range(n)]
x, y, diretion = map(int, input().split())
#현재 좌표 초기화
d[x][y] = 1
#맵 정보 입력
array= []
for i in range(n):
    array.append(list(map(int, input().split())))
#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count=1
turn_time=0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time =0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)

