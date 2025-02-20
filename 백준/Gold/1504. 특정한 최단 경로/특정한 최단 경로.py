import sys
INF = 999999999999999

N, E = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))


def get_smallest(visited, distance):
    smallest_node = 0
    smallest_cost = INF
    for node, cost in enumerate(distance):
        if not visited[node] and cost < smallest_cost:
            smallest_cost = cost
            smallest_node = node

    return smallest_node

def dijkstra(start, end):
    visited = [False for _ in range(N)]
    distance = [INF for _ in range(N)]
    distance[start] = 0

    for _ in range(N):
        node = get_smallest(visited, distance)
        visited[node] = True
        for next, cost in graph[node]:
            if distance[node] + cost < distance[next]:
                distance[next] = distance[node] + cost
    return distance[end]


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