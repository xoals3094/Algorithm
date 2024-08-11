import sys


M, N, H = list(map(int, sys.stdin.readline().strip().split()))

tomato_tower = []
visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

tomato = []

for y in range(H):
    tomato_floor = []
    for z in range(N):
        tomato_line = [int(x) for x in sys.stdin.readline().strip().split()]
        for x, value in enumerate(tomato_line):
            if value == 1:
                tomato.append((x, y, z))
                visit[y][z][x] = 1
            elif value == -1:
                visit[y][z][x] = -1

        tomato_floor.append(tomato_line)
    tomato_tower.append(tomato_floor)


def is_valid_location(x, y, z):
    if not 0 <= x < M:
        return False

    if not 0 <= z < N:
        return False

    if not 0 <= y < H:
        return False

    if visit[y][z][x] == 1:
        return False

    if tomato_tower[y][z][x] == -1:
        return False
    return True


vector = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
days = -1
while len(tomato) > 0:
    temp = []
    for x, y, z in tomato:
        for xv, yv, zv in vector:
            if is_valid_location(x + xv, y + yv, z + zv):
                temp.append((x + xv, y + yv, z + zv))
                visit[y + yv][z + zv][x + xv] = 1

    days += 1
    tomato = temp


def print_result():
    for floor in visit:
        for line in floor:
            if 0 in line:
                print(-1)
                return

    print(days)


print_result()
