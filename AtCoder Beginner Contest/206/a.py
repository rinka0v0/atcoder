import math
n = int(input())

all = math.floor(n*1.08)

if all < 206:
    print('Yay!')
elif all == 206:
    print('so-so')
else:
    print(':(')