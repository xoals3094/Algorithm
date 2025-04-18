import sys
import heapq
from collections import defaultdict

INF = 1e9

N = int(sys.stdin.readline().rstrip())
A = ''.join(list(map(lambda x: str(int(x) - 1),sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())

commands = []
for _ in range(M):
    L, R, C = map(int, sys.stdin.readline().rstrip().split())
    commands.append((L - 1, R - 1, C))

costs = defaultdict(lambda: INF)
def dijkstra(start_arr):
    q = []
    heapq.heappush(q, (0, start_arr))
    costs[start_arr] = 0

    while q:
        cost, arr = heapq.heappop(q)
        if costs[arr] < cost:
            continue

        for l, r, c in commands:
            next = list(arr)
            next[l], next[r] = next[r], next[l]
            next = ''.join(next)
            if costs[arr] + c < costs[next]:
                heapq.heappush(q, (cost + c, next))
                costs[next] = costs[arr] + c

    start_arr = list(start_arr)
    start_arr.sort()
    start_arr = ''.join(start_arr)
    return costs[start_arr]

result = dijkstra(A)
print(result if result != INF else -1)
