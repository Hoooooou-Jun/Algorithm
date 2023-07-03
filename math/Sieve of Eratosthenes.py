import math; 

n1, n2 = map(int, input().split())

res = [True for i in range(n2 + 1)]

for i in range(2, int(math.sqrt(n2)) + 1):
  if res[i] == True:
    j = 2
    while i * j <= n2:
      res[i * j] = False
      j += 1
for i in range(2, n2 + 1):
  if res[i]:
    print(i, end=' ')