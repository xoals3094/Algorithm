import sys


N, M = map(int, sys.stdin.readline().strip().split())
memory = [0] + list(map(int, sys.stdin.readline().strip().split()))
cost = [0] + list(map(int, sys.stdin.readline().strip().split()))
total = sum(cost)
dp = [[0 for _ in range(total + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(total + 1):
        app_memory = memory[i]
        app_cost = cost[i]
        if app_cost > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - app_cost] + app_memory)

result = 1e20
for i in range(1, N + 1):
    for j in range(total + 1):
        if dp[i][j] >= M:
            result = min(result, j)

print(result)