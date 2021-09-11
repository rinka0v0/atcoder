w,h = map(int,input().split())
area = [[0]*(w+2) for i in range(h+2)]
for y in range(h):
    row = list(map(int,input().split()))
    for x in range(w):
        area[y+1][x+1] = row[x]

# yが奇数の時
dydx_odd = [[1,-1],[1,0],[1,1],[0,1],[-1,0],[0,-1]]

# yが偶数の時
dydx_even = [[0,-1],[1,0],[0,1],[-1,1],[-1,0],[-1,-1]]

def bfs(startX,startY,dist):
    count = 0
    que = []
    que.append([startX,startY])
    check = True
    while que:
        x,y = que.pop(0)
        if y % 2 == 0:
            dydx = dydx_even
        else:
            dydx = dydx_odd
        for i in range(6):
            if x + dydx[i][0] < 0 or x + dydx[i][0] > w + 1 or y + dydx[i][1] < 0 or y + dydx[i][1] > h + 1:
                check = False
                continue
            if dist[y+dydx[i][1]][x+dydx[i][0]]:
                continue
            if area[y+dydx[i][1]][x+dydx[i][0]] == 1:
                count += 1
                continue
            dist[y+dydx[i][1]][x+dydx[i][0]] = True
            que.append([x+dydx[i][0],y+dydx[i][1]])
    return check,count 

dist = [[False]*(w+2) for i in range(h+2)]
ans = 0

for x in range(w+2):
    for y in range(h+2):
        if area[y][x] == 1:
            continue
        if dist[y][x]:
            continue
        check, count = bfs(x,y,dist)
        if not check:
            ans += count

print(ans)