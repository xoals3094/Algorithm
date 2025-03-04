import sys
from collections import deque

INF = int(1e9)

N, M, R = map(int, sys.stdin.readline().strip().split())
items = list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(N)]

for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().strip().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))


def total_items(distance):
    count = 0
    for i, dist in enumerate(distance):
        if dist <= M:
            count += items[i]

    return count


def dijkstra(start):
    distance = [INF for _ in range(N)]
    distance[start] = 0
    q = deque([(0, start)])

    while q:
        weight, node = q.popleft()
        if weight > distance[node]:
            continue

        for next, dist in graph[node]:
            if distance[node] + dist < distance[next]:
                distance[next] = distance[node] + dist
                q.append((distance[next], next))

    return total_items(distance)


maximum = 0
for x in range(N):
    maximum = max(maximum, dijkstra(x))

print(maximum)