
import sys

INF = 99999999999999999999999


def bellman_ford(start, end, edges, N):
    distance = [INF for _ in range(N)]
    distance[start] = 0

    for _ in range(N - 1):
        for s, e, t in edges:
            if distance[s] + t < distance[e]:
                distance[e] = distance[s] + t

    for s, e, t in edges:
        if distance[s] + t < distance[e]:
            return -1

    return distance[end]


def can_time_travel():
    N, M, W = map(int, sys.stdin.readline().strip().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().strip().split())
        edges.append((S - 1, E - 1, T))
        edges.append((E - 1, S - 1, T))

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().strip().split())
        edges.append((S - 1, E - 1, -T))

    if bellman_ford(0, 0, edges, N) < 0:
        return "YES"

    return "NO"


TC = int(sys.stdin.readline().strip())
for _ in range(TC):
    print(can_time_travel())
