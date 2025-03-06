import sys
from collections import deque

N = int(sys.stdin.readline().strip())

grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]


VECTOR = (
    (0, -1),
    (-1, 0),
    (1, 0),
    (0, 1)

)

size = 2
count = 0
time = 0


def get_baby_shark():
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 9:
                return x, y


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


def get_best(q, x, y, t):
    for nx, ny, nt in q:
        if nt != t:
            break

        if not 0 < grid[ny][nx] < size:
            continue

        if ny < y:
            x = nx
            y = ny

        elif ny == y and nx < x:
            x = nx
            y = ny

    return x, y


def bfs(x, y):
    global size, count, time

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[y][x] = True
    q = deque([(x, y, 0)])
    while q:
        x, y, t = q.popleft()
        if 0 < grid[y][x] < size :
            x, y = get_best(q, x, y, t)
            count += 1
            if count == size:
                count = 0
                size += 1
            time += t
            return x, y

        for vector_x, vector_y in VECTOR:
            move_x = x + vector_x
            move_y = y + vector_y
            if is_valid(move_x, move_y) and not visited[move_y][move_x] and grid[move_y][move_x] <= size:
                visited[move_y][move_x] = True
                q.append((move_x, move_y, t + 1))

    return -1, -1


def start():
    x, y = get_baby_shark()
    while x != -1 and y != -1:
        grid[y][x] = 0
        x, y = bfs(x, y)

    print(time)

start()