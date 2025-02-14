import sys

N, M = map(int, sys.stdin.readline().strip().split())
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
polyominos = (
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (1, 0), (0, 1), (1, 1)),
    ((0, 0), (1, 0), (0, 1), (0, 2)),
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((0, 0), (0, 1), (0, 2), (1, 1))
)

VERTICAL_SYMMETRIC = (1, -1)
HORIZONTAL_SYMMETRIC = (-1 , 1)

def is_valid_position(x, y):
    if not 0 <= x < M:
        return False

    if not 0 <= y < N:
        return False

    return True


def get_mirrored_all_polyomino(polyomino):
    symmetric_x, symmetric_y = VERTICAL_SYMMETRIC
    vertical = [
        [
            polyomino_x * symmetric_x,
            polyomino_y * symmetric_y
        ]
        for polyomino_x, polyomino_y in polyomino
    ]

    symmetric_x, symmetric_y = HORIZONTAL_SYMMETRIC
    horizontal = [
        [
            polyomino_x * symmetric_x,
            polyomino_y * symmetric_y
        ]
        for polyomino_x, polyomino_y in polyomino
    ]

    return [vertical, horizontal]


def get_rotated_all_polyomino(polyomino):
    degrees_0 = [
        [
            polyomino_x,
            polyomino_y
        ]
        for polyomino_x, polyomino_y in polyomino
    ]

    degrees_90 = [
        [
            polyomino_y,
            -polyomino_x
        ]
        for polyomino_x, polyomino_y in polyomino
    ]

    degrees_180 = [
        [
            -polyomino_x,
            -polyomino_y
        ]
        for polyomino_x, polyomino_y in polyomino
    ]

    degrees_270 = [
        [
            -polyomino_y,
            polyomino_x
        ]
        for polyomino_x, polyomino_y in polyomino
    ]

    return [degrees_0, degrees_90, degrees_180, degrees_270]


def get_all_polyomino():
    all_polyomino = []
    for polyomino in polyominos:
        rotated_polyominos = get_rotated_all_polyomino(polyomino)
        all_polyomino += rotated_polyominos
        for rotated_polyomino in rotated_polyominos:
            all_polyomino += get_mirrored_all_polyomino(rotated_polyomino)

    return all_polyomino


def get_total(polyomino, base_x, base_y):
    total = 0
    for polyomino_x, polyomino_y in polyomino:
        x = polyomino_x + base_x
        y = polyomino_y + base_y
        if not is_valid_position(x, y):
            return 0
        total += grid[y][x]

    return total


def get_max():
    all_polyomino = get_all_polyomino()
    max = 0
    for y in range(N):
        for x in range(M):
            for polyomino in all_polyomino:
                value = get_total(polyomino, x, y)
                if value > max:
                    max = value

    return max

print(get_max())