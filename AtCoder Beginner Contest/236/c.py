from collections import defaultdict

N, M = map(int,input().split())
S = list(input().split())
T = list(input().split())

m = defaultdict(int)

for i in S:
    m[i] = 0

for t in T:
    m[t] = 1

for i in m:
    if m[i] == 1:
        print('Yes')
    else:
        print('No')