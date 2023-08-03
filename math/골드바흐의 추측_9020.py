import math

case = int(input())
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(case):
    num = int(input())
    h = num // 2
    t = num // 2
    for j in range(num // 2):
        if isPrime(h) and isPrime(t):
            print(h, t)
            break
        else:
            h -= 1
            t += 1
