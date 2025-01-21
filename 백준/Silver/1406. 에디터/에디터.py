from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
    cmd = list(stdin.readline().split())
    if cmd[0] == 'L' and left:
        right.append(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

# [::-1]은 리스트를 역순으로 뒤집는 것임
answer = left + right[::-1]
print(''.join(answer))
