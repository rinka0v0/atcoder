l = list(map(int,input().split()))
a = list(map(int,input().split()))
N = l[0]
X = l[1]

all = 0
for i in range(len(a)):
    if i % 2 == 0:
        all += a[i] 
    else:
        all += a[i] -1

if X >= all:
    print('Yes')
else:
    print('No')