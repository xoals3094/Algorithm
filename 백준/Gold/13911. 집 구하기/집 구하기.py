import sys
import heapq

INF = 1e20

V, E = map(int, sys.stdin.readline().split())
MAC = V
STA = V + 1

graph = [[] for _ in range(V + 2)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

M, X = map(int, sys.stdin.readline().split())
for node in map(int, sys.stdin.readline().split()):
    graph[MAC].append((node - 1, 0))

S, Y = map(int, sys.stdin.readline().split())
for node in map(int, sys.stdin.readline().split()):
    graph[STA].append((node - 1, 0))


def dijkstra(start):
    distance = [INF for _ in range(V)]
    q = []
    for node, w in graph[start]:
        distance[node] = 0
        heapq.heappush(q, (0, node))
    while q:
        w, node = heapq.heappop(q)
        if distance[node] < w:
            continue

        for next, w in graph[node]:
            if distance[node] + w < distance[next]:
                distance[next] = distance[node] + w
                heapq.heappush(q, (distance[node] + w, next))

    return distance


def solution():
    result = INF
    for node, d in enumerate(zip(dijkstra(MAC), dijkstra(STA))):
        m, s = d
        if m == 0 or s == 0 or m > X or s > Y:
            continue
        result = min(result, m + s)

    print(result if result != INF else -1)
solution()


