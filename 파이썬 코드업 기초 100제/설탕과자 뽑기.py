h, w = map(int, input().split())
n= int(input())
# stick_info = []
# for i in range(n):
#     stick_info.append(list(map(int, input().split())))
stick_info = [list(map(int, input().split())) for _ in range(n)]
# 막대의 길이(l), 방향(d), 좌표(x, y)
# d:가로는 0, 세로는 1
array = [[0] * w for _ in range(h)]
for j in range(n):
    if stick_info[j][1] == 0:
        l=stick_info[j][0]
        x=stick_info[j][2]
        y=stick_info[j][3]
        for a in range(l):
            array[x-1][y-1+a] =1
    elif stick_info[j][1] == 1:
        l = stick_info[j][0]
        x = stick_info[j][2]
        y = stick_info[j][3]
        for b in range(l):
            array[x -1 + b][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(array[i][j], end=' ')
    print()