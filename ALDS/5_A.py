# TLEする
n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

for i in range(q):
    ans = False
    for j in range(2**n):
        count = 0
        for k in range(n):
            if (j >> k) & 1:
                count += a[k]
                if count > m[i]:
                    break
        if count == m[i]:
            ans = True
    if ans:
        print('yes')
    else:
        print('no')
    
            
