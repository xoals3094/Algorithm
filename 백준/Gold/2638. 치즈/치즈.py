import sys
from collections import deque

VECTOR = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
)

N, M = map(int, sys.stdin.readline().strip().split())

grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]


def is_valid(x, y):
    return 0 <= x < M and 0 <= y < N


def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for vector_x, vector_y in VECTOR:
            move_x = x + vector_x
            move_y = y + vector_y
            if not is_valid(move_x, move_y):
                continue

            if grid[y][x] == 0:
                if visited[move_y][move_x] == 0:
                    q.append((move_x, move_y))
                    visited[move_y][move_x] += 1
                else:
                    visited[move_y][move_x] += 1

    return visited

def melt_cheese(visited):
    target = []
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1 and visited[y][x] >= 2:
                target.append((x, y))

    for x, y in target:
        grid[y][x] = 0

    return len(target)


timer = 0
while melt_cheese(bfs()) > 0:
    timer += 1

print(timer)