n = int(input())
a = list(map(int,input().split()))

a = sorted(a)
ans = True

for i in range(1,n+1):
    if a[i-1] != i:
        ans = False

if ans:
    print('Yes')
else:
    print('No')