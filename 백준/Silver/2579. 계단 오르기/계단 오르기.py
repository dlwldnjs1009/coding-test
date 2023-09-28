stair = int(input())
stair_score = [0]
dp = [0] * (stair+1)


for i in range(stair):
    a = int(input())
    stair_score.append(a)

dp[1] = stair_score[1]
if stair > 1:
    dp[2] = stair_score[1] + stair_score[2]
for j in range(3, stair + 1):
    dp[j] = max(dp[j - 2] + stair_score[j], dp[j - 3] + stair_score[j - 1] + stair_score[j])

print(dp[stair])
