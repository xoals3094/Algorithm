import sys

INF = 999999
RED = 0
GREEN = 1
BLUE = 2


N = int(sys.stdin.readline().strip())
dp = [
    [INF for _ in range(3)]
    for _ in range(N)
]

r, g, b = map(int, sys.stdin.readline().strip().split())
dp[0][RED] = r
dp[0][GREEN] = g
dp[0][BLUE] = b

for i in range(1, N):
    for j, cost in enumerate(map(int, sys.stdin.readline().strip().split())):
        a = dp[i - 1][(j + 1) % 3]
        if dp[i - 1][(j + 1) % 3] + cost < dp[i][j]:
            dp[i][j] = dp[i - 1][(j + 1) % 3] + cost

        b = dp[i - 1][(j + 2) % 3]
        if dp[i - 1][(j + 2) % 3] + cost < dp[i][j]:
            dp[i][j] = dp[i - 1][(j + 2) % 3] + cost

print(min(dp[N - 1]))

