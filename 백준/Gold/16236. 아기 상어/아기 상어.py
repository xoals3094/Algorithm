import sys
import heapq

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


def bfs(x, y):
    global size, count, time

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[y][x] = True
    q = [(0, y, x)]
    while q:
        t, y, x = heapq.heappop(q)
        if 0 < grid[y][x] < size :
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
                heapq.heappush(q, (t + 1, move_y, move_x))

    return -1, -1


def start():
    x, y = get_baby_shark()
    while x != -1 and y != -1:
        grid[y][x] = 0
        x, y = bfs(x, y)

    print(time)

start()