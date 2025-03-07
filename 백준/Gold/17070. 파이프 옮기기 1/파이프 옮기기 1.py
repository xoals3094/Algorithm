import sys

HORIZONTAL = 0
VERTICAL = 1
DIAGONAL = 2

WALL = 1

N = int(sys.stdin.readline().strip())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for y in range(1, N + 1):
    for x, value in enumerate(list(map(int, sys.stdin.readline().strip().split()))):
        graph[y][x + 1] = value


def start():
    dp = [
        [[0, 0 ,0] for _ in range(N + 1)] for _ in range(N + 1)
    ]

    dp[1][2][HORIZONTAL] = 1

    for y in range(1, N + 1):
        for x in range(3, N + 1):
            if graph[y][x] != WALL:
                dp[y][x][HORIZONTAL] = dp[y][x - 1][HORIZONTAL] + dp[y][x - 1][DIAGONAL]
                dp[y][x][VERTICAL] = dp[y - 1][x][VERTICAL] + dp[y - 1][x][DIAGONAL]
                if graph[y - 1][x] != WALL and graph[y][x - 1] != WALL:
                    dp[y][x][DIAGONAL] = dp[y - 1][x - 1][HORIZONTAL] + dp[y - 1][x - 1][VERTICAL] + dp[y - 1][x - 1][DIAGONAL]

    print(dp[N][N][HORIZONTAL] + dp[N][N][VERTICAL] + dp[N][N ][DIAGONAL])

start()