import sys
import copy
from collections import deque

VECTOR = (
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
)

SPACE = 0
WALL = 1
VIRUS = 2

N, M = map(int, sys.stdin.readline().strip().split())

LAB = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
space = []
virus = []

for y in range(N):
    for x in range(M):
        if LAB[y][x] == 0:
            space.append((x, y))
        elif LAB[y][x] == 2:
            virus.append((x, y))

combinations = []
def bt(n, combination):
    if len(combination) == 3:
        combinations.append(combination)
        return

    for i in range(n, len(space)):
        bt(i + 1, combination + [i])

bt(0, [])

def is_valid(x, y):
    return 0 <= x < M and 0 <= y < N

def safety_area(new_wall):
    lab = copy.deepcopy(LAB)
    for x, y in new_wall:
        lab[y][x] = WALL

    q = deque(virus.copy())
    while q:
        x, y = q.popleft()
        for vector_x, vector_y in VECTOR:
            move_x = x + vector_x
            move_y = y + vector_y
            if is_valid(move_x, move_y) and lab[move_y][move_x] != WALL and lab[move_y][move_x] != VIRUS:
                lab[move_y][move_x]= VIRUS
                q.append((move_x, move_y))

    area = 0
    for y in range(N):
        for x in range(M):
            if lab[y][x] == SPACE:
                area += 1

    return area

maximum = 0
for combination in combinations:
    new_wall = [space[i] for i in combination]
    maximum = max(maximum, safety_area(new_wall))

print(maximum)