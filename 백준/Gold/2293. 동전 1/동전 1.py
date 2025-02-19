n, k = map(int, input().split())

value = []
for i in range(n):
    value.append(int(input()))


dp = [0] * (k + 1)
dp[0] = 1
for c in value:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]

print(dp[k])
