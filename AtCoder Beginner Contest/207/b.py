import math
l = list(map(int,input().split()))
a = l[0]
b = l[1]
c = l[2]
d = l[3]


if c*d > b :
    print(math.ceil(a/(c*d-b)))
else:
    print(-1)
