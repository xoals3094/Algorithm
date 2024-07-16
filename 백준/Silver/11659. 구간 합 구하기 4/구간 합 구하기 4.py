import sys


N, M = map(int, sys.stdin.readline().strip().split())

section = list(map(int, sys.stdin.readline().strip().split()))
dp = [0]

for i, value in enumerate(section):
    dp.append(value + dp[i])


for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(dp[j] - dp[i - 1])
