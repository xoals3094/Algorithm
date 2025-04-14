import sys
INF = 1e9

N = int(sys.stdin.readline())
ALL = (1 << N) - 1

W = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[-1 for _ in range(1 << N)] for _ in range(N)]

def travel(start, visited):
    if visited == ALL:
        return W[start][0] if W[start][0] != 0 else INF

    if dp[start][visited] != -1:
        return dp[start][visited]

    dp[start][visited] = INF
    for next in range(1, N):
        if visited & 1 << next or W[start][next] == 0:
            continue

        dp[start][visited] = min(dp[start][visited], travel(next, visited | 1 << next) + W[start][next])

    return dp[start][visited]

print(travel(0, 1))
