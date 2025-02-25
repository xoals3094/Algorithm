import sys

N, M = map(int, sys.stdin.readline().strip().split())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for n in range(1, N + 1):
    line = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, N + 1):
        dp[n][i] = dp[n][i - 1] + dp[n - 1][i] - dp[n - 1][i - 1] + line[i - 1]


for _ in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().strip().split())
    print(
        dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1]
    )
