n = input()
length = len(n)
n = int(n)

s = 998244353 

ans = 0
# n - 1 桁の計算
for i in range(length - 1):
    ans += ((1 / 2) * ((9*10**i) % s ) * ((1 + 9*10**i) % s )) % s
    # ans %= s

# n桁目の計算
N = (((n - 10**(length - 1))) % s + 1) % s 
ans += ((1 / 2) * N * (N + 1))  % s

ans = ans % s

print(int(ans))