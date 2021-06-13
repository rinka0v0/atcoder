import sys
sys.setrecursionlimit(10000000)

H,W = map(int,input().split())


dx = [1,0,-1,0]
dy = [0,1,0,-1]

field = []

seen = list([False for i in range(W)] for j in range(H))

for i in range(H):
    field.append(input())

def dfs (h,w):
    seen[h][w] = True

    for i in range(4):
        nexth = h + dy[i]
        nextw = w + dx[i]
        if nexth < 0 or nexth >= H or nextw < 0 or nextw >= W:
            continue
        if (field[nexth][nextw] == '#'):
            continue
        if (seen[nexth][nextw]):
            continue
        dfs(nexth,nextw)
            

for i in range(H):
    for j in range(W):
        if field[i][j] == 's':
            starth = i
            startw = j
        if field[i][j] == 'g':
            goalh = i
            goalw = j

dfs(starth,startw)

if (seen[goalh][goalw]):
    print('Yes')
else:
    print('No')
 