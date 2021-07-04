l = list(map(int,input().split()))
a = l[0]
b = l[1]

if a <= b and b <= 6*a:
    print('Yes')
else:
    print('No')