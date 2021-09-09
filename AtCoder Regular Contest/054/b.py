#（解法1） 手計算で微分し、導関数が0になるxを求める
import math
p = float(input())

x = 1.5 * math.log2((p*math.log(2))/1.5)

y = x + p/(2**(x/1.5))

if x >= 0:
    print(y)
else:
    print(p)

#(解法2) 導関数が0になるxを2分法を用いて求める。
import math

p = float(input())

def f(x):
    return (1 - (1/(3/2))*p*math.log(2)*2**(-x/(3/2)))

def isOk(value):
    if f(value) >= 0:
        return True
    else:
        return False


right = 10**18
left  = 0
while right - left > 0.000000001:
    mid = right - (right - left) / 2
    if isOk(mid):
        right = mid
    else:
        left = mid
x = right

print(x + p/(2**(x/1.5)))
