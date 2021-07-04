l = list(map(int,input().split()))
n = l[0]
k = l[1]
a = list(map(int,input().split()))

ans = list((k//n) for i in range(n))
ls = sorted(a)

num = ls[k%n]

for i in range(n):
    if a[i] < num:
        ans[i] += 1

for j in ans:
    print(j)
