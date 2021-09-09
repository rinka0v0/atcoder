n  = int(input())
ls = [list(map(int,input().split())) for i in range(n)]

seen       = [False for i in range(n)]
first_time = [0 for i in range(n)]
last_time  = [0 for i in range(n)]

g = [[] for i in range(n)]

for i in ls:
    for j in range(i[1]):
        g[i[0]-1].append(i[2+j] - 1)

def dfs(g,v,t):
    t += 1
    first_time[v] = t
    seen[v] = True
    for i in g[v]:
        if seen[i]:
            continue
        t = dfs(g,i,t)
    t += 1
    last_time[v] = t
    return t

t = 0
for i in range(len(seen)):
    if seen[i] == False:
        t = dfs(g,i,t)

for i in range(n):
    print(i+1,first_time[i],last_time[i])
