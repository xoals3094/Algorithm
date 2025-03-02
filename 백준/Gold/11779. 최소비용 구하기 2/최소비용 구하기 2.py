import sys
import heapq

INF = int(10e20)

WEIGHT = 0
PARENT = 1

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, w))


def dijkstra(start):
    distance = [[INF, -1] for _ in range(N + 1)]
    q = []
    distance[start][WEIGHT] = 0
    heapq.heappush(q, (0, start))
    while q:
        w, node = heapq.heappop(q)
        if w > distance[node][WEIGHT]:
            continue
        for next, weight in graph[node]:
            if distance[node][WEIGHT] + weight < distance[next][WEIGHT]:
                distance[next][WEIGHT] = distance[node][WEIGHT] + weight
                distance[next][PARENT] = node
                heapq.heappush(q, (distance[next][WEIGHT], next))

    return distance


def get_path(end, distance):
    parent = end
    path = []
    while parent != -1:
        path.append(parent)
        parent = distance[parent][PARENT]
    path.reverse()
    return path


def print_result():
    start, end = map(int, sys.stdin.readline().strip().split())
    distance = dijkstra(start)
    path = get_path(end, distance)
    print(distance[end][WEIGHT])
    print(len(path))
    print(' '.join(list(map(str, path))))

print_result()