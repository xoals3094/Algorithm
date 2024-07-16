import sys


class Value:
    def __init__(self, zero, one):
        self.zero = zero
        self.one = one


T = int(sys.stdin.readline().strip())

dp = {
    0: Value(1, 0),
    1: Value(0, 1)
}  # n : Value


def fibonacci(n):
    zero = dp[n - 2].zero + dp[n - 1].zero
    one = dp[n - 2].one + dp[n - 1].one

    dp[n] = Value(zero, one)


for _ in range(T):
    N = int(sys.stdin.readline().strip())
    for x in range(2, N + 1):
        fibonacci(x)

    print(dp[N].zero, dp[N].one)


