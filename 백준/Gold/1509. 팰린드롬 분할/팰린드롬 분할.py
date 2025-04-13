import sys

string = sys.stdin.readline().rstrip()

dp = [[False for _ in string] for _ in string]
for i in range(len(string)):
    dp[i][i] = True

for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        dp[i][i + 1] = True


for i in range(len(string) - 3, -1, -1):
    for j in range(i + 2, len(string)):
        if dp[i + 1][j - 1] and string[i] == string[j]:
            dp[i][j] = True


def solution():
    split = [1e20 for _ in range(len(string) + 1)]
    split[-1] = 0

    for end in range(len(string)):
        for start in range(end + 1):
            if dp[start][end]:
                split[end] = min(split[end], split[start - 1] + 1)
            else:
                split[end] = min(split[end], split[end - 1] + 1)
    return split[-2]

print(solution())
