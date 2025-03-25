import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N + 1)]
degrees = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    graph[A].append(B)
    degrees[B] += 1

def topology_sort():
    q = deque()
    for node in range(1, N + 1):
        if degrees[node] == 0:
            q.append(node)
    result = []
    for _ in range(N):
        node = q.popleft()
        result.append(node)
        for next in graph[node]:
            degrees[next] -= 1
            if degrees[next] == 0:
                q.append(next)

    return result

print(' '.join(list(map(str, topology_sort()))))