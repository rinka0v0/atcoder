p = list(map(int,input().split()))

alpha = 'abcdefghijklmnopqrstuvwxyz'
ans = []

for i in p:
    ans.append(alpha[i-1])

for i in ans:
    print(i,end='')
