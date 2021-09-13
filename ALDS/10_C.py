# これだとTLEになる
q = int(input())

ls = [input() for i in range(q*2)]

for i in range(0,q*2,2):
    a,b = ls[i],ls[i+1]
    dp = [[0]*(len(b) + 1) for i in range(len(a) + 1)]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i+1][j+1] = max(dp[i][j] + 1,dp[i+1][j],dp[i][j+1])
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    print(dp[len(a)][len(b)])

