# B  How Many Islands?

# 再帰回数の上限を変更しないとエラーになる
import sys
sys.setrecursionlimit(10000)


dh = [0,1,1,1,0,-1,-1,-1]
dw = [1,1,0,-1,-1,-1,0,1]

def dfs (h,w):
    seen[h][w] = True

    for i in range(len(dh)):
        nexth = h + dh[i]
        nextw = w + dw[i]
        if nextw < 0 or W <= nextw or nexth < 0 or H <= nexth:
            continue
        if seen[nexth][nextw]:
            continue
        dfs(nexth, nextw)

while True:
    W, H = map(int,input().split())

    if W == 0 and H == 0:
        break

    seen = list(list(False for i in range(W)) for j in range(H))

    field = list(list(map(int,input().split())) for i in range(H))

    for i in range(H):
        for j in range(W):
            if field[i][j] == 0:
                seen[i][j] = True

    count = 0

    for i in range(H):
        for j in range(W):
            if seen[i][j]:
                continue
            dfs(i,j)
            count += 1

    print(count)


