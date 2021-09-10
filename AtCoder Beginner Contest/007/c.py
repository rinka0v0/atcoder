r,c = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
area = [input() for i in range(r)]

dist = [[-1]*c for i in range(c)]
dist[sy - 1][sx - 1] = 0

dx = [1,0,-1,0]
dy = [0,-1,0,1]
que = []
que.append([sy - 1,sx - 1])

while que:
    y,x = que.pop(0)
    for i in range(4):
        if dist[y+dy[i]][x+dx[i]] != -1:
            continue
        if area[y+dy[i]][x+dx[i]] == '#':
            continue
        dist[y+dy[i]][x+dx[i]] = dist[y][x] + 1
        que.append([y+dy[i],x+dx[i]])

print(dist[gy - 1][gx - 1])
    