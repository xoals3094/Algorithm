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

def is_melting(x, y, external_air):
    count = 0
    for vector_x, vector_y in VECTOR:
        move_x = x + vector_x
        move_y = y + vector_y
        if is_valid(move_x, move_y) and external_air[move_y][move_x]:
            count += 1
    return count >= 2


def bfs():
    external_air = [[False for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0)])
    external_air[0][0] = True
    while q:
        x, y = q.popleft()
        for vector_x, vector_y in VECTOR:
            move_x = x + vector_x
            move_y = y + vector_y
            if not is_valid(move_x, move_y):
                continue

            if not external_air[move_y][move_x] and grid[move_y][move_x] == 0:
                external_air[move_y][move_x] = True
                q.append((move_x, move_y))

    return external_air

def melt_cheese(external_air):
    target = []
    for y in range(N):
        for x in range(M):
            if not external_air[y][x] and grid[y][x] == 1 and is_melting(x, y, external_air):
                target.append((x, y))

    for x, y in target:
        grid[y][x] = 0

    return len(target)


timer = 0
while melt_cheese(bfs()) > 0:
    timer += 1

print(timer)