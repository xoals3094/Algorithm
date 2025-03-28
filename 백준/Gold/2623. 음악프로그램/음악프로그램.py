import sys
from collections import deque


N, M = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N + 1)]
degrees = [0 for _ in range(N + 1)]
for _ in range(M):
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, len(sequence) - 1):
        node = sequence[i]
        next = sequence[i + 1]
        graph[node].append(next)
        degrees[next] += 1


def topology_sort():
    q = deque()
    for i in range(1, len(degrees)):
        if degrees[i] == 0:
            q.append(i)

    result = []
    for _ in range(N):
        if len(q) == 0:
          return [0]

        node = q.popleft()
        result.append(node)
        for next in graph[node]:
            degrees[next] -= 1
            if degrees[next] == 0:
                q.append(next)
    return result


for seq in topology_sort():
    print(seq)