import sys
input = sys.stdin.readline

# 초기 문자열 읽기
initial_string = input().rstrip()
M = int(input().rstrip())

left_stack = list(initial_string)  
right_stack = []                   

for _ in range(M):
    command = input().split()
    op = command[0]

    if op == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif op == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif op == 'B':
        if left_stack:
            left_stack.pop()
    elif op == 'P':
        left_stack.append(command[1])

print(''.join(left_stack + right_stack[::-1]))
