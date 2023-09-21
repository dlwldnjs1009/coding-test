from collections import deque

n = int(input())
# 6입력 123456
# 1버리고 2 맨 밑으로
# 34562
# 3버리고 4 맨 밑으로
# 5624
# 5버리고 6 맨 밑으로
# 246
# 2버리고 4 맨 밑으로
# 64
# 6버리고 4남음
array = [i for i in range(1, n+1)]
q = deque()
for j in range(len(array)):
    q.append(array[j])



while q:
    if len(q) == 1:
        a = q.popleft()
        print(a)
        break
    q.popleft()
    a = q.popleft()
    q.append(a)

