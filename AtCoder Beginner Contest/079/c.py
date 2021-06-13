a,b,c,d = input()
l = [['-']*3 for i in range(2**3)]

for i in range(2**3):
  for j in range(3):
    if i >> j & 1 == 1:
      l[i][j] = '+'
      
for i in l:
    if eval(a + i[0] + b + i[1] + c + i[2] + d) == 7:
        print(a + i[0] + b + i[1] + c + i[2] + d + '=7') 
        break

n = int(input())
l = map(int,input().split())
count = 0

for i in l:
    if i > 10:
        count += i - 10

print(count)