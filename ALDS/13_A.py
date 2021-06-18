# 8 クイーン問題
import itertools

k = int(input())
queen = list(list(map(int,input().split())) for i in range(k)) 
board = list('.'*8 for i in range(8))

all = list(itertools.permutations(range(8)))
comb = list(itertools.combinations(range(8),2))

for i in all:
    count = True
    for j in comb:
        x,y = j[0],j[1]
        if  abs(i[x]-i[y]) == abs(x - y):
            count = False
    if count:
        for j in range(k):
            x,y = queen[j]
            if i[x] != y:
                count = False
                break
    if count:
        ans = i
        break

for i in range(8):
    print('.'*ans[i] + 'Q' + '.'*(7-ans[i]))

