n,m = map(int,input().split())

l = list(list(map(int,input().split())) for i in range(n))

ans = 0
for i in range(m-1):
    for j in range(i+1,m):
        all = 0
        for k in range(n):
            all += max(l[k][i],l[k][j])
        ans = max(all,ans)

print(ans)

