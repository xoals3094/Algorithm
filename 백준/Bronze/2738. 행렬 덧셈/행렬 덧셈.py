import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for y in range(N):
    for x in range(M):
        print(A[y][x] + B[y][x], end=' ')
    print()