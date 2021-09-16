# 1年生
n = int(input())
ls = list(map(int,input().split()))

dp=[[0]*21 for i in range(n+1)]
dp[1][ls[0]] = 1

for i in range(n):
    for j in range(21):
        if 0 <= (j + ls[i]) <= 20:
            dp[i+1][j] += dp[i][j+ls[i]]
        if 0 <= (j - ls[i]) <= 20:
            dp[i+1][j] += dp[i][j-ls[i]]

print(dp[n-1][ls[n-1]])
