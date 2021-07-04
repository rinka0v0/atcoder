import math
p = int(input())

ans = 0
while p > 0:
    for i in range(1,11):
        kaijo = math.factorial(i)
        if kaijo <= p and p < math.factorial(i+1) and i < 10:
            ans +=  p // kaijo 
            p = p%(kaijo)
            break
        elif i > 9:
            ans += p // kaijo
            p =  p%(kaijo)
            break

print(ans)
