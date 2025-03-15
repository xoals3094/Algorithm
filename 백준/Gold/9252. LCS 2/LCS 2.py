import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()


dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lcs = []
i = len(B)
j = len(A)
while dp[i][j] != 0:
    if dp[i][j] == dp[i][j - 1]:
        j = j - 1
    elif dp[i][j] == dp[i - 1][j]:
        i = i - 1
    else:
        lcs.append(A[j - 1])
        i = i - 1
        j = j - 1

lcs.reverse()

print(len(lcs))
for x in lcs:
    print(x, end='')
