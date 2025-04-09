import sys
from collections import deque

VECTOR = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
)

N, M = map(int, sys.stdin.readline().strip().split())

grid = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
parents = [x for x in range(N * M)]
counts = [0 for _ in range(N * M)]

def is_valid(x, y):
    if 0 <= x < M and 0 <= y < N:
        return True

    return False


def bfs(x, y):
    if visited[y][x] or grid[y][x] == 1:
        return

    count = 1
    root = M * y + x
    visited[y][x] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        parents[M * y + x] = root
        for mx, my in VECTOR:
            if is_valid(x + mx, y + my) and not visited[y + my][x + mx] and grid[y + my][x + mx] == 0:
                visited[y + my][x + mx] = True
                q.append((x + mx, y + my))
                count += 1

    counts[root] = count



def get_root(x, y):
    return parents[M * y + x]


for y in range(N):
    for x in range(M):
        bfs(x, y)


for y in range(N):
    for x in range(M):
        if grid[y][x] == 1:
            total = 1
            roots = []
            for mx, my in VECTOR:
                if is_valid(x + mx, y + my):
                    roots.append(get_root(x + mx, y + my))

            for root in set(roots):
                total += counts[root]

            print(total % 10, end='')
        else:
            print(0, end='')
    print()