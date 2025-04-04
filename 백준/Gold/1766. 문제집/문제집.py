import sys
import heapq


N, M = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N + 1)]
degrees = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    graph[A].append(B)
    degrees[B] += 1

q = []
for i in range(1, len(degrees)):
    if degrees[i] == 0:
        heapq.heappush(q, i)

for _ in range(N):
    node = heapq.heappop(q)
    print(f'{node}', end=' ')
    for next in graph[node]:
        degrees[next] -= 1
        if degrees[next] == 0:
            heapq.heappush(q, next)
