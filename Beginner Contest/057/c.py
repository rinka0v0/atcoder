import math
n = int(input())
ans = 1000
for i in range(1,math.floor(n**(1/2))+1):
    if n%i ==0:
        b = n//i
        rank = len(str(b))
        ans = min(ans,rank)

print(ans)