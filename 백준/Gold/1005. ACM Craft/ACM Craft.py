import sys
from collections import deque


T = int(sys.stdin.readline().strip())


def acm_craft():
    N, K = map(int, sys.stdin.readline().strip().split())
    costs = list(map(int, sys.stdin.readline().strip().split()))
    degrees = [0 for _ in range(N)]
    times = [0 for _ in range(N)]
    graph = [[] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a - 1].append(b - 1)
        degrees[b - 1] += 1

    W = int(sys.stdin.readline().strip()) - 1
    q = []
    for num, degree in enumerate(degrees):
        if degree == 0:
            times[num] = costs[num]
            q.append(num)

    q = deque(q)
    for _ in range(N):
        num = q.popleft()
        for next in graph[num]:
            times[next] = max(times[next], times[num] + costs[next])
            degrees[next] -= 1
            if degrees[next] == 0:
                q.append(next)

    return times[W]

for _ in range(T):
    print(acm_craft())
