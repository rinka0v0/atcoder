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