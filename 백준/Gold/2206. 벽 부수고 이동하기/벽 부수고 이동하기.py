import sys

VECTOR = (
    (0, 1),
    (0, - 1),
    (1, 0),
    (-1, 0)
)

NOT_USED = 0
USED = 1

N, M = map(int, sys.stdin.readline().strip().split())

graph = [list(map(int, list(sys.stdin.readline().strip())))for _ in range(N)]
visited = [
    [
        [False, False] for _ in range(M)
    ] for _ in range(N)
]


def is_valid_position(x, y):
    if 0 <= x < M and 0 <= y < N:
        return True
    return False

def bfs(x, y):
    count = 1
    visited[y][x] = [True, True]
    q = [(x, y, NOT_USED)] # x, y, chance
    while q:
        tmp = q
        q = []
        for x, y, chance in tmp:
            if x == M - 1 and y == N - 1:
                return count

            for x_vector, y_vector in VECTOR:
                x_position = x + x_vector
                y_position = y + y_vector
                if not is_valid_position(x_position, y_position):
                    continue

                if visited[y_position][x_position][chance]:
                    continue

                if graph[y_position][x_position] == 1 and chance == USED:
                    continue

                if graph[y_position][x_position] == 1 and chance == NOT_USED:
                    q.append((x_position, y_position, USED))
                    visited[y_position][x_position][chance] = True
                    continue

                q.append((x_position, y_position, chance))
                visited[y_position][x_position][chance] = True
        count += 1

    return -1

print(bfs(0, 0))
