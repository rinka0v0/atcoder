# abc 150 B
n = int(input())
s = input()
count = 0
 
for i in range(n-2):
  if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
    count += 1
        
print(count)

# abc 122 B
s = input()
ans = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
        count = 1
        if i == len(s) - 1:
            ans = max(ans,count)
            break
        else:
            for j in range(i+1, len(s)):
                if  s[j] == 'A' or s[j] == 'C' or s[j] == 'G' or s[j] == 'T':
                    count += 1
                    ans = max(ans,count)
                else:
                    ans = max(ans,count)
                    break

print(ans)

# 解説
S = input()
N = len(S)
ans = 0
for i in range(N):
    for j in range(i, N):
        if all('ACGT'.count(c) == 1 for c in S[i:j+1]):
            ans = max(ans,j=i+1)
print(ans)


# abc136 B
n = int(input())
count = 0

for i in range(1,n+1):
    string = str(i)
    if len(string)%2 == 1:
        count += 1

print(count)

# abc106 B
n = int(input())
ans = 0

for i in range(1,n+1,2):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 8:
        ans += 1
print(ans)

# abc12- B
a,b,k = map(int,input().split())
count = 0
for i in range(min(a,b),0,-1):
    if a % i == b % i == 0:
        count += 1
        if count == k:
            print(i)
            break

# abc057 C
import math
n = int(input())
ans = 1000
for i in range(1,math.floor(n**(1/2))+1):
    if n%i ==0:
        b = n//i
        rank = len(str(b))
        ans = min(ans,rank)

print(ans)

# abc096 C
a,b,c,x,y = map(int,input().split())
ans = 5000*10**10

if x >= y:
    for i in range(x+1):
        if i <=y:
            money = 2*c*i + a*(x-i) + b*(y-i)
            ans = min(ans,money)
        else:
            money = 2*c*i + a*(x-i)
            ans = min(ans,money)
else:
    for i in range(y+1):
        if i <=x:
            money = 2*c*i + a*(x-i) + b*(y-i)
            ans = min(ans,money)
        else:
            money = 2*c*i + b*(y-i)
            ans = min(ans,money)

print(ans)

a,b,c,x,y = map(int,input().split())
ans = 5000*10**10

for i in range(max(x,y)+1):
    money = 2*c*i + a*max(0,x-i) + b*max(0,y-i)
    ans = min(ans,money)

print(ans)

#  abc079 C

a,b,c,d = input()
l = [['-']*3 for i in range(2**3)]

for i in range(2**3):
  for j in range(3):
    if i >> j & 1 == 1:
      l[i][j] = '+'
      
for i in l:
    if eval(a + i[0] + b + i[1] + c + i[2] + d) == 7:
        print(a + i[0] + b + i[1] + c + i[2] + d + '=7') 
        break

n = int(input())
l = map(int,input().split())
count = 0

for i in l:
    if i > 10:
        count += i - 10

print(count)

#  C

n,m = map(int,input().split())

l = list(list(map(int,input().split())) for i in range(n))
a = [0] * n
b = [0] * m
for i in range(n):
  a[i] = l[i][0]
for i in range(m):
  b[i] = l[i][1]

count = 0  
for i in range(n):
    count += 1
    if b[i] in a:
        j = i
        while True:
            ind = a.index(b[j])
            count += 1
            if b[ind] not in a or a[i] == b[ind]:
                break
            else:
                j = a.index(b[ind])
    else:
        break
print(count)

#  D
n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
for i in range(0 ,n , 2):
    count += l[i]


# sumitb2019_D

n = int(input())
s = input()
count = 0
for i in range(1000):
    j = str(i).zfill(3)
    S = s
    for k in range(3):
        index = S.find(j[k])
        if index != -1 :
            S = S[index+1:]
            if k == 2:
                count += 1
        else:
            break

print(count)

# 128 C

n,m = map(int,input().split())
switchNumber = []
bulb = []
ans = 0

for i in range(m):
    l = list(map(int,input().split()))
    switchNumber.append(l[0])
    switch= l[1:]
    bulb.append(switch)
p = list(map(int,input().split()))
print(bulb)
print(switchNumber)

for i in range(2**m):
    a = True
    for j in range(m):
        count = 0
        print(j)
        for k in range(switchNumber[j]):
            print(k)
            print(bulb[j][k])
            count +=  i >> (bulb[j][k] -1) & 1 
        if count%2 != p[j]:
            a = False
            break
    if a :
        ans += 1
print(ans)

# 128 回答

n,m = map(int,input().split())
switchNumber = []
bulb = []
ans = 0

for i in range(m):
    l = list(map(int,input().split()))
    switchNumber.append(l[0])
    switch= l[1:]
    bulb.append(switch)
p = list(map(int,input().split()))
# print(bulb)
# print(switchNumber)

for i in range(2**n):
    a = True
    # print(i,'i')
    for j in range(m):
        count = 0
        # print(j,'j')
        for k in range(switchNumber[j]):
            # print(k,'k')
            # print(bulb[j][k],'bulb[j][k]')
            count +=  i >> (bulb[j][k] -1) & 1 
        if count%2 != p[j]:
            a = False
            break
    if a :
        ans += 1

print(ans)

#  147 C

n = int(input())
say = []
ans = 0

for i in range(n):
    a = int(input())
    l=[]
    for j in range(a):
        l.append(list(map(int,input().split())))
    say.append(l)

for i in range(2**n):
    correct = True
    for j in range(n):
        if i >> j & 1 == 1:
            for k in range(len(say[j])):
                if (say[j][k][1] == 1 and i >> say[j][k][0] - 1 & 1 ==  0) or  (say[j][k][1] == 0 and i >> say[j][k][0] - 1 & 1 ==1):
                    correct = False
                    break
    if correct and i != 0 and j == n-1:
        number = 0
        for x in range(n):
            if i >> x & 1 == 1:
                number += 1
        ans = max(number,ans)

print(ans)

#  abc 150 C
import itertools 
n = int(input())
p = list(map(int,input().split()))
p = str(p)
strp = ''
for i in p:
    stri = str(i)
    strp += stri
q = list(map(int,input().split()))
q = str(q)
strq = ''
for i in q:
    stri = str(i)
    strq += stri
all = []
for i in range(1,n+1):
    all.append(i)

l = list(itertools.permutations(all))
length = len(list(itertools.permutations(all)))
for i in range(length):
    if l[i][0] == p[0] and l[i][1] == p[1] and l[i][2] == p[2]:
        a = i
    if l[i][0] == q[0] and l[i][1] == q[1] and l[i][2] == q[2]:
        b = i

print(b-a)

# print(all)



# 回答 150 C 
import itertools 
n = int(input())
p = list(map(int,input().split()))
strp = ''
for i in p:
    stri = str(i)
    strp += stri

q = list(map(int,input().split()))
strq = ''
for i in q:
    stri = str(i)
    strq += stri

all = []
for i in range(1,n+1):
    stri = str(i)
    all.append(stri)

l = list(itertools.permutations(all))
length = len(l)
print(l[0][0] ,l[0][1] ,l[0][2],'l')
for i in range(length):
    if l[i][0] == strp[0] and l[i][1] == strp[1] and l[i][2] == strp[2]:
        a = i
    if l[i][0] == strq[0] and l[i][1] == strq[1] and l[i][2] == strq[2]:
        b = i
# print(a,'a')
# print(b,'b')

print(abs(b-a))

#ABC150C
import itertools

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
ls = list(itertools.permutations(range(1,n+1))) #順列生成
print(abs(ls.index(p)-ls.index(q)))

import itertools

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
ls = list(itertools.permutations(range(1,n+1))) #順列生成
for i in range(len(ls)):
    if ls[i] == p:
        a = i
    if ls[i] == q:
        b = i
print(abs(a-b))

# abc 145 - C
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

#  abc 054 C
import itertools
n,m = map(int,input().split())
paths = [list(map(int,input().split())) for i in range(m)]

all = list(itertools.permutations(range(1,n+1)))
ans = 0

for i in range(len(all)):
    count = True
    if all[i][0] != 1:
        break
    for j in range(n-1):
        now = all[i][j]
        next = all[i][j+1]
        path = [min(now,next), max(now,next)]
        print([now,next])
        if (path not in paths):
            count = False
            break
    if count:
        ans += 1

print(ans)

