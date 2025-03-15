import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()


dp = [['' for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + A[j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=lambda x: len(x))

print(len(dp[len(B)][len(A)]))
print(dp[len(B)][len(A)])
