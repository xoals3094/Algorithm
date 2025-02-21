import sys

N = int(sys.stdin.readline().strip())
dp = [0 for _ in range(N + 1)]

dp[1] = int(sys.stdin.readline().strip())
for _ in range(N - 1):
    new_dp = [0 for _ in range(N + 1)]
    nodes = list(map(int, sys.stdin.readline().strip().split()))
    nodes.insert(0, 0)
    for i in range(1, len(nodes)):
        node = nodes[i]
        new_dp[i] = max(dp[i - 1] + node, dp[i] + node)
    dp = new_dp

print(max(dp))




