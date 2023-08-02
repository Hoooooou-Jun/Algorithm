import itertools

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

nmArr = list(itertools.permutations(arr, m))

for j in nmArr:
    print(' '.join(map(str, j)))