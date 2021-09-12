n,w = map(int,input().split())
ls = [list(map(int,input().split())) for i in range(n)]

dp = [[0]*(w+10) for i in range(n+1)]

for i in range(n):
    for j in range(w+1):
        if ls[i][1] <= j:
            dp[i+1][j] = max(dp[i][j],dp[i+1][j-ls[i][1]] + ls[i][0])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[n][w])