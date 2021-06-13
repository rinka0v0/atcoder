import itertools
n,m = map(int,input().split())
paths = [list(map(int,input().split())) for i in range(m)]

all = list(itertools.permutations(range(1,n+1)))
ans = 0

for i in range(len(all)):
    count = True
    if all[i][0] != 1:
        break
    for j in range(n-1):
        now = all[i][j]
        next = all[i][j+1]
        path = [min(now,next), max(now,next)]
        print([now,next])
        if (path not in paths):
            count = False
            break
    if count:
        ans += 1

print(ans)