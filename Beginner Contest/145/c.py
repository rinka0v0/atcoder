import itertools
n = int(input())
ans = 0
all =  [list(map(int,input().split())) for i in range(n)]

ls = list(itertools.permutations(range(1,n+1)))


for i in range(len(ls)):
    ave = 0
    for j in range(n-1):
        now = ls[i][j] - 1
        next = ls[i][j+1] - 1
        ave += ((all[now][0] - all[next][0])**2 + (all[now][1] -all[next][1])**2)**(1/2)
    ans += ave

print(ans/len(ls))