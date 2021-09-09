# 再帰回数の上限を変更しないとrecursion Errorとなる

import sys
sys.setrecursionlimit(200000)
w,h = map(int,input().split())
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

def dfs(c,x,y):
    c[x][y] = 0
    for i in range(8):
        if x+dx[i] < 0 or x+dx[i] >= h or y+dy[i] < 0 or y+dy[i] >= w:
            continue
        if c[x+dx[i]][y+dy[i]] == 0:
            continue
        dfs(c,x+dx[i],y+dy[i])

while w != 0 or h != 0:
    c = [list(map(int,input().split())) for i in range(h)]
    count = 0
    for x in range(h):
        for y in range(w):
            if c[x][y] == 0:
                continue
            dfs(c,x,y)
            count += 1
    print(count)
    w,h = map(int,input().split())

