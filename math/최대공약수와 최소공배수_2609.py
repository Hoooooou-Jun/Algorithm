a, b = map(int, input().split())
lcm = 0

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        lcm = i
        break

print(int((a * b) / i))