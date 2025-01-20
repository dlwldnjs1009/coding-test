from collections import deque

n = int(input())
stack = deque([])
for i in range(n):
    op = input().split(' ')
    if op[0] == 'push_front':
        stack.appendleft(int(op[1]))
    elif op[0] == 'push_back':
        stack.append(int(op[1]))
    elif op[0] == 'pop_front':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack.popleft())
    elif op[0] == 'pop_back':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack.pop())
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        if len(stack) == 0 :
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[0])
    elif op[0] == 'back':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[-1])
