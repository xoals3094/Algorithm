import sys
N, M = map(int, sys.stdin.readline().strip().split())

visit = [[False for _ in range(M)] for _ in range(N)]
distance = [[-1 for _ in range(M)] for _ in range(N)]

goal_x = 0
goal_y = 0
grid = []
for y in range(N):
    line = list(map(int, sys.stdin.readline().strip().split()))
    for x, value in enumerate(line):
        if value == 2:
            goal_x = x
            goal_y = y

        if value == 0:
            distance[y][x] = 0
    grid.append(line)


def is_valid_coor(x, y):
    if x < 0 or x >= M:
        return False

    if y < 0 or y >= N:
        return False

    if grid[y][x] == 0:
        return False

    return True


def bfs():
    q = [(goal_x, goal_y)]
    visit[goal_y][goal_x] = True
    depth = 0
    while len(q) > 0:
        temp = []
        for (x, y) in q:
            distance[y][x] = depth
            if is_valid_coor(x + 1, y) and not visit[y][x + 1]:
                visit[y][x + 1] = True
                temp.append((x + 1, y))

            if is_valid_coor(x - 1, y) and not visit[y][x - 1]:
                visit[y][x - 1] = True
                temp.append((x - 1, y))

            if is_valid_coor(x, y + 1) and not visit[y + 1][x]:
                visit[y + 1][x] = True
                temp.append((x, y + 1))

            if is_valid_coor(x, y - 1) and not visit[y - 1][x]:
                visit[y - 1][x] = True
                temp.append((x, y - 1))
        depth += 1
        q = temp


bfs()
for line in distance:
    for x in line:
        print(x, end=' ')
    print()