import sys

BIT = 2 ** 10


def solution():
    N = int(sys.stdin.readline())
    if N == 1:
        return 0

    dp = [[[0 for _ in range(BIT)] for _ in range(10)] for _ in range(N)]

    for current in range(1, 9):
        dp[1][current - 1][1 << current | 1 << current - 1] += 1
        dp[1][current + 1][1 << current | 1 << current + 1] += 1

    dp[1][9 - 1][1 << 9 | 1 << 9 - 1] += 1

    for n in range(1, N - 1):
        for current in range(10):
            for mask, count in enumerate(dp[n][current]):
                if count > 0:
                    if 0 < current < 9:
                        dp[n + 1][current + 1][mask | (1 << current + 1)] += count
                        dp[n + 1][current - 1][mask | (1 << current - 1)] += count

                    elif current == 0:
                        dp[n + 1][current + 1][mask | (1 << current + 1)] += count

                    elif current == 9:
                        dp[n + 1][current - 1][mask | (1 << current - 1)] += count


    total = 0
    for current in range(10):
        total += dp[N - 1][current][BIT - 1]
    return total % 1000000000

print(solution())