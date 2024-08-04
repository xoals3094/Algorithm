import sys

N, M = map(int, sys.stdin.readline().strip().split())

campus = [list(sys.stdin.readline().strip()) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
q = []

for y, line in enumerate(campus):
    for x, value in enumerate(line):
        if value == 'I':
            q.append((x, y))
            visit[y][x] = True

def is_valid_location(x, y):
    if not 0 <= x < M:
        return False
    if not 0 <= y < N:
        return False
    if campus[y][x] == 'X':
        return False
    if visit[y][x]:
        return False

    return True


count = 0
while len(q) > 0:
    x, y = q.pop()
    if campus[y][x] == 'P':
        count += 1

    if is_valid_location(x - 1, y):
        q.append((x - 1, y))
        visit[y][x - 1] = True

    if is_valid_location(x + 1, y):
        q.append((x + 1, y))
        visit[y][x + 1] = True

    if is_valid_location(x, y - 1):
        q.append((x, y - 1))
        visit[y - 1][x] = True

    if is_valid_location(x, y + 1):
        q.append((x, y + 1))
        visit[y + 1][x] = True


print('TT' if count == 0 else count)