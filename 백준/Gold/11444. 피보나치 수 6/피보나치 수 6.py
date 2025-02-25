import sys

mod = 1_000_000_007

N = int(sys.stdin.readline().strip())
dp = {}

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    if n in dp:
        return dp[n]

    elif n % 2 == 0:
        dp[n] = (fibonacci(n // 2) * (fibonacci(n // 2 + 1) + fibonacci(n // 2 - 1))) % mod
        return dp[n]

    elif n % 2 == 1:
        dp[n] = (fibonacci((n + 1) // 2) ** 2 + fibonacci((n - 1) // 2) ** 2) % mod
        return dp[n]

print(fibonacci(N))
