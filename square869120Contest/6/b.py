n = int(input())

all = list(list(map(int,input().split())) for i in range(n))
ans = 10**100

for s in range(n):
    for e in range(n):
        start = all[s][0]
        end = all[e][1]
        count = 0
        for i in range(n):
            count += abs(start-all[i][0]) + abs(all[i][0] - all[i][1]) + abs(end - all[i][1])
        ans = min(ans,count)

print(ans)