import sys
from collections import deque


INF = 999999999

N, K = map(int, sys.stdin.readline().strip().split())

distance = [INF for _ in range(100_000 * 2 + 1)]


def bfs(start, end):
    q = deque([(start, 0)])

    while q:
        node, weight = q.popleft()
        if node == end:
            return weight

        if weight >= distance[node]:
            continue

        distance[node] = weight
        if node * 2 <= K + 1:
            q.appendleft((node * 2, weight + 0))
        if node + 1 <= K + 1:
            q.append((node + 1, weight + 1))
        if node - 1 >= 0:
            q.append((node - 1, weight + 1))

print(bfs(N, K))