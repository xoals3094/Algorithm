import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

def lcs(str1, str2, str3):
    dp = [[[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)] for _ in range(len(str3) + 1)]
    for i in range(1, len(str3) + 1):
        for j in range(1, len(str2) + 1):
            for k in range(1, len(str1) + 1):
                if str1[k - 1] == str2[j - 1] and str1[k - 1] == str3[i - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[len(str3)][len(str2)][len(str1)]


print(lcs(A, B, C))
