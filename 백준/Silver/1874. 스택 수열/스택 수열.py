count = 1
temp = True
stack = []
op = []

n = int(input())
for i in range(n):
    num = int(input())
    # num 이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
