import sys 
import copy
sys.setrecursionlimit(1000000)

ans = False

dh = [0,1,0,-1]
dw = [1,0,-1,0]

field = list(input() for i in range(10))

seen = list(list(False for i in range(10)) for j in range(10))

for i in range(10):
    for j in range(10):
        if field[i][j] == 'x':
            seen[i][j] = True

def dfs(h,w,s):
    s[h][w] = True
     
    for i in range(4):
        nextH = h + dh[i]
        nextW = w + dw[i]
        if nextH < 0 or 10 <= nextH or nextW < 0 or 10 <= nextW:
            continue
        if s[nextH][nextW]:
            continue
        dfs(nextH,nextW,s)

for i in range(10):
    for j in range(10):
        seenCopy = copy.deepcopy(seen)
        seenCopy[i][j] = False
        dfs(i,j,seenCopy)

        count = True
        for height in range(10):
            for width in range(10):
                if seenCopy[height][width] == False:
                    count = False
        if count:
            ans = True

if ans:
    print('YES')
else:
    print('NO')
