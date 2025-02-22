import sys
import heapq

INF = 999999999999999999

N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    S, E, W = map(int, sys.stdin.readline().strip().split())
    tree[S - 1].append((E - 1, W))
    tree[E - 1].append((S - 1, W))


def dijkstra(start):
    distance = [INF for _ in range(N)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        weight, node = heapq.heappop(q)
        if weight < distance[node]:
            continue

        for next, weight in tree[node]:
            if distance[node] + weight < distance[next]:
                distance[next] = distance[node] + weight
                heapq.heappush(q, (distance[next], next))

    max_node = 0
    max_distance = 0
    for node, distance in enumerate(distance):
        if distance > max_distance:
            max_distance = distance
            max_node = node

    return max_node, max_distance


n1, distance = dijkstra(0)
n2, distance = dijkstra(n1)

print(distance)