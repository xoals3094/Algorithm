import sys

INF = int(1e20)

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

distance = [
    [INF for _ in range(N)]
    for _ in range(N)
]

for x in range(N):
    distance[x][x] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    distance[a - 1][b - 1] = min(distance[a - 1][b - 1], c)


def floyd():
    for waypoint in range(N):
        for start in range(N):
            for end in range(N):
                distance[start][end] = min(distance[start][end], distance[start][waypoint] + distance[waypoint][end])

floyd()
for nodes in distance:
    print(" ".join(
            map(lambda node: str(node) if node < INF else str(0), nodes)
        )
    )