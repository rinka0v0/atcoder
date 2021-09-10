import sys
sys.setrecursionlimit(200000000)

def input():
    return sys.stdin.readline()[:-1]

n,q = map(int,input().split())
g = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

p = [list(map(int,input().split())) for i in range(q)]

counter = [0 for i in range(n)]
for i in p:
    counter[i[0]-1] += i[1]

counter.append(0)

def dfs(v,p):
    counter[v] += counter[p]
    for i in g[v]:
        if i == p:
            continue
        # counter[i] += counter[v]
        dfs(i,v)

dfs(0,-1)

for j in range(n):
    print(counter[j],end=' ')