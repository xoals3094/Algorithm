import sys
INF = 99999999999999999

N, M, B = map(int, sys.stdin.readline().strip().split())

grid = []
for _ in range(N):
    grid.append([int(x) for x in sys.stdin.readline().strip().split()])


def get_total_block(goal_floor):
    exceed_block = 0
    need_block = 0

    for line in grid:
        for cell in line:
            rest = goal_floor - cell
            if rest > 0:
                need_block += rest
                continue

            exceed_block += abs(rest)

    return exceed_block, need_block


def get_time_at_floor(goal_floor):
    exceed_block, need_block = get_total_block(goal_floor)
    if exceed_block + B < need_block:
        return INF

    return (exceed_block * 2) + need_block


time = INF
h = 0
for floor in range(257):
    used_time_at_floor = get_time_at_floor(floor)
    if time >= used_time_at_floor:
        time = used_time_at_floor
        h = floor

print(time, h)
