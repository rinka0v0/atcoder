h,w = map(int,input().split())
s = [input() for i in range(h)]
white = 0
for x in range(h):
    for y in range(w):
        if s[x][y] == '.':
            white += 1

dxdy = [[0,1],[-1,0],[0,-1],[1,0]]

dist = [[-1]*w for i in range(h)]
dist[0][0] = 0
que = []
que.append([0,0])
while que:
    x,y = que.pop(0)
    for i in range(4):
        if x+dxdy[i][0] < 0 or x+dxdy[i][0] > h - 1 or y+dxdy[i][1] < 0 or y+dxdy[i][1] > w - 1:
            continue
        if dist[x+dxdy[i][0]][y+dxdy[i][1]] != -1:
            continue
        if s[x+dxdy[i][0]][y+dxdy[i][1]] == '#':
            continue
        dist[x+dxdy[i][0]][y+dxdy[i][1]] = dist[x][y] + 1
        que.append([x+dxdy[i][0],y+dxdy[i][1]])

if dist[h-1][w-1] == -1:
    print(-1)
else:
    print(white - dist[h-1][w-1] - 1)

