import sys

D = int(sys.stdin.readline())

MATRIX = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]



def mul(a, b):
    c = [[0 for _ in range(8)] for _ in range(8)]
    for y in range(8):
        for x in range(8):
            for i in range(8):
                c[y][x] = (c[y][x] + (a[y][i] * b[i][x]) % 1_000_000_007) % 1_000_000_007
    return c


dp = {
    1: MATRIX,
    2: mul(MATRIX, MATRIX)
}

def pow(n):
    if n in dp:
        return dp[n]

    if n % 2 == 0:
        dp[n] = mul(pow(n // 2), pow(n // 2))
        return dp[n]

    else:
        dp[n] = mul(pow(n - 1), MATRIX)
        return dp[n]

print(pow(D)[0][0])
