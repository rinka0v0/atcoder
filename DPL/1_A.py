N,M = map(int,input().split())
c = list(map(int,input().split()))

dp = [[10**5]*(N+1) for i in range(M+1)]
dp[0][0] = 0

for i in range(M):
    for n in range(N+1):
        if c[i] <= n:
            dp[i+1][n] = min(dp[i][n],dp[i+1][n-c[i]] + 1)
        else:
            dp[i+1][n] = dp[i][n]

print(dp[M][N])