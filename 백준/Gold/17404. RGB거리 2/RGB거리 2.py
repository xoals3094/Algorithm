import sys
INF = 1e20

R = 0
G = 1
B = 2

N = int(sys.stdin.readline().strip())
street = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]


def rgb_min(start):
    dp = [INF for _ in range(3)]
    dp[start] = street[0][start]

    for i, rgb in enumerate(street[1:]):
        i += 1
        r, g, b = rgb
        new_dp = [INF for _ in range(3)]

        new_dp[G] = min(new_dp[G], dp[R] + g)
        new_dp[B] = min(new_dp[B], dp[R] + b)

        new_dp[B] = min(new_dp[B], dp[G] + b)
        new_dp[R] = min(new_dp[R], dp[G] + r)

        new_dp[R] = min(new_dp[R], dp[B] + r)
        new_dp[G] = min(new_dp[G], dp[B] + g)
        dp = new_dp

    del dp[start]
    return min(dp)

result = INF
for s in [R, G, B]:
    result = min(result, rgb_min(s))

print(result)
