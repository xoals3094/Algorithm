import sys
INF = 999999999999999

N, E = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))


def dijkstra(start, end) -> int:
    dk = [INF for _ in range(N)]
    dk[start] = 0
    q = [start]
    while len(q) > 0:
        node = q.pop(0)
        for next, distance in graph[node]:
            if dk[node] + distance < dk[next]:
                dk[next] = dk[node] + distance
                q.append(next)
    return dk[end]


def get_result():
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    v1 -= 1
    v2 -= 1
    a_to_b = 0
    a_to_b += dijkstra(0, v1)
    a_to_b += dijkstra(v1, v2)
    a_to_b += dijkstra(v2, N - 1)

    b_to_a = 0
    b_to_a += dijkstra(0, v2)
    b_to_a += dijkstra(v2, v1)
    b_to_a += dijkstra(v1, N - 1)

    result = -1
    if min(a_to_b, b_to_a) < INF:
        result = min(a_to_b, b_to_a)
    return result


print(get_result())