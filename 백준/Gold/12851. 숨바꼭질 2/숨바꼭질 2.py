import sys
import heapq

INF = int(1e10)
WEIGHT = 0
COUNT = 1

N, K = map(int, sys.stdin.readline().strip().split())

MAX = 100_000 * 2

def dijkstra(start, end):
    distance = [[INF, 0] for _ in range(MAX + 1)]
    distance[start][WEIGHT] = 0
    distance[start][COUNT] = 1
    q = [(0, start)]

    while q:
        weight, node = heapq.heappop(q)
        if weight > distance[node][WEIGHT]:
            continue

        if node * 2 <= MAX and distance[node][WEIGHT] + 1 <= distance[node * 2][WEIGHT]:
            if distance[node][WEIGHT] + 1 == distance[node * 2][WEIGHT]:
                distance[node * 2][COUNT] += distance[node][COUNT]
                continue

            distance[node * 2][WEIGHT] = distance[node][WEIGHT] + 1
            distance[node * 2][COUNT] = distance[node][COUNT]
            heapq.heappush(q, (distance[node * 2][WEIGHT], node * 2))

        if node + 1 <= MAX and distance[node][WEIGHT] + 1 <= distance[node + 1][WEIGHT]:
            if distance[node][WEIGHT] + 1 == distance[node + 1][WEIGHT]:
                distance[node + 1][COUNT] += distance[node][COUNT]
                continue

            distance[node + 1][WEIGHT] = distance[node][WEIGHT] + 1
            distance[node + 1][COUNT] = distance[node][COUNT]
            heapq.heappush(q, (distance[node + 1][WEIGHT], node + 1))

        if node - 1 >= 0 and distance[node][WEIGHT] + 1 <= distance[node - 1][WEIGHT]:
            if distance[node][WEIGHT] + 1 == distance[node - 1][WEIGHT]:
                distance[node - 1][COUNT] += distance[node][COUNT]
                continue

            distance[node - 1][WEIGHT] = distance[node][WEIGHT] + 1
            distance[node - 1][COUNT] = distance[node][COUNT]
            heapq.heappush(q, (distance[node - 1][WEIGHT], node - 1))

    return distance[end][WEIGHT], distance[end][COUNT]

d, c = dijkstra(N, K)
print(d, c)