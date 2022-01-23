n = int(input())
A = list(map(int,input().split()))

ans = [0] * n

for a in A:
    ans[a - 1] += 1

for i in range(len(ans)):
    if ans[i] == 3:
        print(i + 1)
