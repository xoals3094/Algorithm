import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
MAX = 100_000

def bfs(start, end):
    visited = [False for _ in range(MAX + 1)]
    visited[start] = True
    q = deque([(start, 0)])
    minimum = 0
    count = 0
    while q:
        node, weight = q.popleft()
        if node == end and not visited[end]:
            count += 1
            minimum = weight

        elif node == end and minimum == weight:
            count += 1

        visited[node] = True
        for next in [node * 2, node + 1, node - 1]:
            if 0 <= next <= MAX and not visited[next]:
                q.append((next, weight + 1))


    return minimum, count

t, cnt = bfs(N, K)
print(t)
print(cnt)