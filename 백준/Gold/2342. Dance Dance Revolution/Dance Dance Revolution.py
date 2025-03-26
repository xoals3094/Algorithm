import sys
INF = 99999999999
seq = list(map(int, sys.stdin.readline().strip().split()))

dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(seq))]
dp[0][0][0] = 0

def move(current, next):
    if current == 0:
        return 2
    elif abs(current - next) == 2:
        return 4
    elif current == next:
        return 1
    else:
        return 3

for i in range(len(seq) - 1):
    n = seq[i]
    for l in range(5):
        for r in range(5):
            dp[i + 1][l][n] = min(dp[i + 1][l][n], dp[i][l][r] + move(r, n))
            dp[i + 1][n][r] = min(dp[i + 1][n][r], dp[i][l][r] + move(l, n))

print(min(map(min, dp[len(dp)-1])))