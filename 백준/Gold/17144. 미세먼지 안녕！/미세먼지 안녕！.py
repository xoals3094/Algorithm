import sys

R, C, T = map(int, sys.stdin.readline().strip().split())
CLEANER = -1
UP = 0
DOWN = 1

VECTOR = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
)

room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]

air_cleaner = []
for y in range(R):
    for x in range(C):
        if room[y][x] == -1:
            air_cleaner.append((x, y))

def is_valid(x, y):
    return 0 <= x < C and 0 <= y < R

def find_dust():
    dusts = []
    for y in range(R):
        for x in range(C):
            if room[y][x] > 0:
                dusts.append((x, y))

    return dusts


def diffuse(dusts):
    diffused_dusts = [] # (origin_x, origin_y, move_x, move_y, value)
    for x, y in dusts:
        for vx, vy in VECTOR:
            mx = x + vx
            my = y + vy
            if is_valid(mx, my) and room[my][mx] != CLEANER:
                diffused_dusts.append((x, y, mx, my, room[y][x] // 5))

    return diffused_dusts


def apply(diffused_dusts):
    for ox, oy, mx, my, v in diffused_dusts:
        room[oy][ox] -= v
        room[my][mx] += v
        
def work_air_cleaner():
    cx, cy = air_cleaner[UP]
    for y in range(cy - 2, -1, -1):
        room[y + 1][cx] = room[y][cx]
        room[y][cx] = 0

    for x in range(1, C):
        room[0][x - 1] = room[0][x]
        room[0][x] = 0

    for y in range(1, cy + 1):
        room[y - 1][C - 1] = room[y][C - 1]
        room[y][C - 1] = 0

    for x in range(C - 2, 0, -1):
        room[cy][x + 1] = room[cy][x]
        room[cy][x] = 0

    dx, dy = air_cleaner[DOWN]
    for y in range(dy + 2, R):
        room[y - 1][dx] = room[y][dx]
        room[y][dx] = 0

    for x in range(1, C):
        room[R - 1][x - 1] = room[R - 1][x]
        room[R - 1][x] = 0

    for y in range(R - 2, cy , -1):
        room[y + 1][C - 1] = room[y][C - 1]
        room[y][C - 1] = 0

    for x in range(C - 2, 0, -1):
        room[dy][x + 1] = room[dy][x]
        room[dy][x] = 0

def start():
    for _ in range(T):
        dusts = find_dust()
        diffused_dusts = diffuse(dusts)
        apply(diffused_dusts)
        work_air_cleaner()

    total = 0
    for y in range(R):
        for x in range(C):
            if room[y][x] > 0:
                total += room[y][x]

    return total

print(start())