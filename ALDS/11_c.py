n = int(input())
ls = [list(map(int,input().split())) for i in range(n)]

g = [[] for i in range(n)]

for i in range(n):
    k = ls[i][1]
    for j in range(k):
        g[ls[i][0] - 1].append(ls[i][j+2] - 1)


dist = [-1 for i in range(n)]
que = []
que.append(0)
dist[0] = 0

while que:
    v = que.pop(0)
    for i in g[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        que.append(i)

for i in range(n):
    print(i+1,dist[i])