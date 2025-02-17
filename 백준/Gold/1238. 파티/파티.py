import sys

INF = 9999999999999999

N, M, X = map(int, sys.stdin.readline().strip().split())
X -= 1
graph = [[] for _ in range(N)]


for _ in range(M):
    A, B, T = map(int, sys.stdin.readline().strip().split())
    graph[A - 1].append((B - 1, T))


def dijkstra(start, end) -> int:
    dk = [INF for _ in range(N)]
    dk[start] = 0
    q = [start]
    while len(q) > 0:
        node = q.pop(0)
        for next, time in graph[node]:
            if dk[node] + time < dk[next]:
                dk[next] = dk[node] + time
                q.append(next)

    return dk[end]

max = 0
for n in range(N):
    go_to_party = dijkstra(n, X)
    back_to_home = dijkstra(X, n)
    if max < go_to_party + back_to_home:
        max = go_to_party + back_to_home

print(max)