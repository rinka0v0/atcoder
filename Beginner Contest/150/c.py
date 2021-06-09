import itertools

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
ls = list(itertools.permutations(range(1,n+1))) #順列生成
for i in range(len(ls)):
    if ls[i] == p:
        a = i
    if ls[i] == q:
        b = i
print(abs(a-b))