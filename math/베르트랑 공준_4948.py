import math

nums = []
while True:
    num = int(input())
    if (num == 0):
        break
    nums.append(num)

for i in range(len(nums)):
    a = nums[i]
    b = nums[i] * 2
    arr = [True for i in range(b + 1)]
    res = 0
    for j in range(2, int(math.sqrt(b)) + 1):
        if arr[j] == True:
            h = 2
            while j * h <= b:
                arr[j * h] = False
                h += 1
    for m in range(a + 1, b + 1):
        if arr[m]:
            if m != 1:
                res += 1
    print(res)