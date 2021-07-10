n  = int(input())
c = list(map(int,input().split()))

c.sort()
num = 10**9 + 7
count = 1

for i in range(len(c)):
    if i+1 <= c[i]:
        count *= c[i] - i 
        count = count % num
    else:
        count = 0
        break

print(count % (10**9 + 7))