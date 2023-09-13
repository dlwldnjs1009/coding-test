#1부터 계속 더하다가 200이 되면 종료
s = int(input())
result = 0
i=1
while result < s:
    if result + i > s:
        break
    result += i
    i += 1

print(i-1)

# n이 1부터 증가해서

