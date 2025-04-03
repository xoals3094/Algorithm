import sys
import heapq

WEIGHT = 0
VALUE = 1

N, K = map(int, sys.stdin.readline().rstrip().split())

gems = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
bags = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

gems.sort(key=lambda x: x[0])
bags.sort()

q = []
total = 0
i = 0
for bag in bags:
    while i < N and gems[i][WEIGHT] <= bag:
        heapq.heappush(q, -gems[i][VALUE])
        i += 1
    if q:
        total += -heapq.heappop(q)

print(total)