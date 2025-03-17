# 이걸 어떻게 풀어야 할까?

n = int(input())

calendar = [0] * 366

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        calendar[i] += 1
        
row = 0
col = 0
result = 0

for day in calendar:
    if day != 0:
        col = max(col, day)
        row += 1
    
    else:
        result += row * col
        row = 0
        col = 0
result += row * col
print(result)
