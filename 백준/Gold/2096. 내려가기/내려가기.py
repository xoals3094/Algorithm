import sys

N = int(sys.stdin.readline().strip())

min_dp = list(map(int, sys.stdin.readline().strip().split()))
max_dp = min_dp.copy()

for _ in range(1, N):
    new_min_dp = [0 for _ in range(3)]
    new_max_dp = [0 for _ in range(3)]

    a, b, c = map(int, sys.stdin.readline().strip().split())
    new_max_dp[0] = max(max_dp[0] + a, max_dp[1] + a)
    new_min_dp[0] = min(min_dp[0] + a, min_dp[1] + a)

    new_max_dp[1] = max(max_dp[0] + b, max_dp[1] + b, max_dp[2] + b)
    new_min_dp[1] = min(min_dp[0] + b, min_dp[1] + b, min_dp[2] + b)

    new_max_dp[2] = max(max_dp[1] + c, max_dp[2] + c)
    new_min_dp[2] = min(min_dp[1] + c, min_dp[2] + c)

    max_dp = new_max_dp
    min_dp = new_min_dp

print(max(max_dp), min(min_dp))