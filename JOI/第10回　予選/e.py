# pythonだとTLE
h,w,n = map(int,input().split())
area = [input() for i in range(h)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]
plant = [[] for i in range(n+1)]

ans = 0
for x in range(h):
    for y in range(w):
        if area[x][y] == 'S':
            plant[0] = [x,y]
        else:
            for i in range(1,n+1):
                if area[x][y] == str(i):
                    plant[i] = [x,y]

def earliest(startX,startY,endX,endY):
    dist = [[-1]*w for i in range(h)]
    dist[startX][startY] = 0
    que = []
    que.append([startX,startY])
    while que:
        x,y = que.pop(0)
        for i in range(4):
            if x+dx[i] < 0 or x+dx[i] > h - 1 or y+dy[i] < 0 or y+dy[i] > w - 1:
                continue
            if dist[x+dx[i]][y+dy[i]] != -1:
                continue
            if area[x+dx[i]][y+dy[i]] == 'X':
                continue
            dist[x+dx[i]][y+dy[i]] = dist[x][y] + 1
            que.append([x+dx[i],y+dy[i]])
    return dist[endX][endY]

ans = 0
for i in range(n):
    ans += earliest(plant[i][0],plant[i][1],plant[i+1][0],plant[i+1][1])
print(ans)