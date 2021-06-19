# 過去に解いたことがある問題

#  ABC106 B
n = int(input())
ans = 0

for i in range(1, n+1):
    count = 0
    if i % 2 == 1:
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
    if count == 8:
        ans += 1

print(ans)

# 122 B 
s = input()
ACGT = 'ACGT'

ans = 0

for i in range(len(s)):
    if s[i] in ACGT:
        count = 1
        if i == len(s) -1:
            ans = max(ans,count)
        for j in range(i+1,len(s)):
            if s[j] in ACGT:
                count += 1
                ans = max(ans,count)
            else:
                ans = max(ans,count)
                break

print(ans)

# ALDS1_5_A  TLEになってしまう

n = int(input())
A = list(map(int,input().split()))
q = int(input())
B = list(map(int,input().split()))
ans = list(False for i in range(q))

for i in range(2**n):
    count = 0
    for j in range(n):
        if i >> j & 1 == 1:
            count += A[j]
    for k in range(q):
        if count == B[k]:
            ans[k] = True

for i in ans:
    if i:
        print('yes')
    else:
        print('no')


# 128 C 

n,m = map(int,input().split())
switch = list(list(map(int,input().split())) for i in range(m))
p = list(map(int,input().split()))
number = 0

for i in range(2**n):
    ans = True
    for j in range(m):
        switchNumber = switch[j][0] 
        count = 0
        for k in range(1,switchNumber + 1):
            if i >> (switch[j][k]-1) & 1 == 1:
                count += 1
        if count % 2 != p[j]:
            ans = False
            break
    if ans:
        number += 1

print(number)



# 150C
import itertools

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))


all = list(itertools.permutations(range(1,n+1)))

for i in range(len(all)):
    if all[i] == p:
        a = i
    if all[i] == q:
        b = i

print(abs(a-b))


# 145 C
import itertools
n = int(input())
ans = 0

coordinate = list(list(map(int,input().split())) for i in range(n))

all = list(itertools.permutations(range(n)))
allLength = len(all)

for i in range(allLength):
    dis = 0
    for j in range(n-1):
        nowx = coordinate[all[i][j]][0]
        nowy = coordinate[all[i][j]][1]
        nextx = coordinate[all[i][j+1]][0]
        nexty = coordinate[all[i][j+1]][1]
        dis += ((nowx-nextx)**2 + (nowy-nexty)**2)**(1/2)
    ans += dis


print(ans/allLength)

