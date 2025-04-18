import sys
import heapq
from collections import defaultdict

INF = 1e9

N = int(sys.stdin.readline().rstrip())
A = list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())

commands = []
for _ in range(M):
    L, R, C = map(int, sys.stdin.readline().rstrip().split())
    commands.append((L - 1, R - 1, C))

costs = defaultdict(lambda: INF)
def dijkstra(start_arr):
    q = []
    heapq.heappush(q, (0, start_arr))
    costs[''.join(list(map(str, start_arr)))] = 0

    while q:
        cost, arr = heapq.heappop(q)
        if costs[''.join(list(map(str, arr)))] < cost:
            continue

        for l, r, c in commands:
            next = arr.copy()
            next[l], next[r] = next[r], next[l]
            if costs[''.join(list(map(str, arr)))] + c < costs[''.join(list(map(str, next)))]:
                heapq.heappush(q, (cost + c, next))
                costs[''.join(list(map(str, next)))] = costs[''.join(list(map(str, arr)))] + c

    start_arr.sort()
    return costs[''.join(list(map(str, start_arr)))]

result = dijkstra(A)
print(result if result != INF else -1)
