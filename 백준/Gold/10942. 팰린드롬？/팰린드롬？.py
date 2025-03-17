import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N):
    i = N - i - 1
    for j in range(i, N):
        if arr[i] == arr[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1


for _ in range(M):
    s, e = map(int, sys.stdin.readline().strip().split())
    print(dp[s - 1][e - 1])
