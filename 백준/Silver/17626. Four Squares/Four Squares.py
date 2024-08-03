import sys
INF = 4

n = int(sys.stdin.readline().strip())

dp = [INF for _ in range(n + 1)]

for x in range(1, n + 1):
    if x ** 2 > n:
        break
    dp[x ** 2] = 1


def calculate_min_squares_count(number):
    x = 1
    square = x ** 2
    while square <= number:
        value = dp[square] + dp[number - square]
        if value < dp[number]:
            dp[number] = value
        x += 1
        square = x**2


for x in range(1, n + 1):
    calculate_min_squares_count(x)
print(dp[n])
