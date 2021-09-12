N,W = map(int,input().split())
ls = [[0,0] for i in range(N+10)]
for i in range(N):
    ls[i] = list(map(int,input().split()))

dp = [[0]*(W+10) for i in range(N+10)]

for i in range(N+1):
    for w in range(W+1):
        if w >= ls[i][1]:
            dp[i+1][w] = max(dp[i][w],dp[i][w-ls[i][1]] + ls[i][0])
        else:
            dp[i+1][w] = dp[i][w]

print(dp[N][w])