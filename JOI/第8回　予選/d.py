import copy
import sys
sys.setrecursionlimit(10**6)
m = int(input())
n = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ace = [list(map(int,input().split())) for i in range(n)]
ans = 0

def dfs(x,y,seen,count):
    seen[x][y] = 0
    splitnum = [0]
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] > n -1 or y + dy[i] < 0 or y + dy[i] > m - 1:
            continue
        if seen[x+dx[i]][y+dy[i]] == 0:
            continue
        splitnum.append(dfs(x+dx[i],y+dy[i],seen,count))
    seen[x][y] = 1
    count += max(splitnum)
    return count + 1


for i in range(n):
    for j in range(m):
        if ace[i][j] == 0:
            continue
        seen = copy.deepcopy(ace)
        total = dfs(i,j,seen,0)
        ans = max(total,ans)
        
print(ans)