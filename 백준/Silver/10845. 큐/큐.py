from collections import deque

n = int(input())
# 반복문 돌면서 입력이랑 문장 if하면 되는거 아닌가
stack = deque([])
for i in range(n):
    # 구분자로 잘라서 리스트에 저장 안의 문자에 따라 if로 나누기
    op = input().split(' ')
    if op[0] == 'push':
        stack.append(int(op[1]))
    elif op[0] == 'pop':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack.popleft())
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
