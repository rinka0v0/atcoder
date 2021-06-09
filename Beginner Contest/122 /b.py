s = input()
ans = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
        count = 1
        if i == len(s) - 1:
            ans = max(ans,count)
            break
        else:
            for j in range(i+1, len(s)):
                if  s[j] == 'A' or s[j] == 'C' or s[j] == 'G' or s[j] == 'T':
                    count += 1
                    ans = max(ans,count)
                else:
                    ans = max(ans,count)
                    break

print(ans)

# 解説
S = input()
N = len(S)
ans = 0
for i in range(N):
    for j in range(i, N):
        if all('ACGT'.count(c) == 1 for c in S[i:j+1]):
            ans = max(ans,j=i+1)
print(ans)