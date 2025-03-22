import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    for x in range(i - 1, j):
        arr[x] = k

print(' '.join(list(map(str, arr))))