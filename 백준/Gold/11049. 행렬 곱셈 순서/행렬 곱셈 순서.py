import sys

N = int(sys.stdin.readline().strip())

INF = 2**31

matrix = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
d = [matrix[0][0]] + [m[1] for m in matrix]

for i in range(N + 1):
    dp[i][i] = 0

for diagonal in range(1, N + 1):
    for i in range(1, N - diagonal + 1):
        j = i + diagonal
        for k in range(1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + d[i - 1] * d[k] * d[j])

print(dp[1][N])

