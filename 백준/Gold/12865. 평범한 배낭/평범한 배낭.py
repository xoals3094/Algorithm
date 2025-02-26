import sys

N, K = map(int, sys.stdin.readline().strip().split())

items = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0 for _ in range(K + 1)] for _ in range(N)]
w, v = items[0]
for k in range(0, K + 1):
    if w <= k:
        dp[0][k] = v


for n in range(1, N):
    w, v = items[n]
    for k in range(K + 1):
        if w > k:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - w] + v)

print(dp[N - 1][K])