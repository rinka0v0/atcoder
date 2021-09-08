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


# 2回目
import itertools
k = int(input())
piece = [list(map(int,input().split())) for i in range(k) ]

ls = list(itertools.permutations(range(8)))
ans = ['.'*8 for i in range(8)]

for i in range(len(ls)):
    ok = True
    for j in range(8):
        for k in range(j+1,8):
            if abs(k - j) == abs(ls[i][k] - ls[i][j]):
                ok = False
    if ok:
        for j in piece:
            judge = True
            for k in range(8):
                if [k,ls[i][k]] == j:
                    judge = False
            if judge:
                ok = False
    if ok:
        for j in range(8):
            print('.'*ls[i][j] + 'Q' + '.'*(7-ls[i][j]))
        break