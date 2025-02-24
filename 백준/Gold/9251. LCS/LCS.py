import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

dp = [
    [0 for _ in range(len(A) + 1)]
    for _ in range(len(B) + 1)
]

for y in range(1, len(B) + 1):
    for x in range(1, len(A) + 1):
        if A[x - 1] == B[y - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
            continue

        dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])

result = 0
for y in range(1, len(B) + 1):
    for x in range(1, len(A) + 1):
        result = max(result, dp[y][x])

print(result)