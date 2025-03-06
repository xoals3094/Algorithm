import sys
from collections import deque

A, B = map(int, sys.stdin.readline().strip().split())


def bfs(start, end):
    q = deque([(start, 0)])

    while q:
        x, count = q.popleft()
        if x == end:
            return count + 1

        for next in [x * 2, (x * 10) + 1]:
            if next <= B:
                q.append((next, count + 1))

    return -1

print(bfs(A, B))
