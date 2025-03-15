import sys

LEN = 0
LCS = 1

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()


dp = [[[0, ''] for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:
            dp[i][j][LEN] = dp[i - 1][j - 1][LEN] + 1
            dp[i][j][LCS] = dp[i - 1][j - 1][LCS] + A[j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=lambda x: x[LEN])

l, lcs = dp[len(B)][len(A)]
print(l)
print(lcs)
