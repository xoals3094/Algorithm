import sys
import heapq

INF = 99999999999999999

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N)]

for _ in range(M):
    S, E, D = map(int, sys.stdin.readline().strip().split())
    graph[S - 1].append((E - 1, D))


S, E = map(int, sys.stdin.readline().strip().split())

def dijkstra(start, end):
    distance = [INF for _ in range(N)]
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue

        for next, cost in graph[node]:
            if distance[node] + cost < distance[next]:
                distance[next] = distance[node] + cost
                heapq.heappush(q, (distance[next], next))

    return distance[end]

print(dijkstra(S - 1, E - 1))