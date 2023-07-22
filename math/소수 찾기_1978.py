count = int(input())
num = list(map(int, input().split()))
res = 0

for i in range(count):
    for j in range(2, num[i] + 1):
        if num[i] % j == 0:
            if num[i] == j:
                res += 1
            break

print(res)