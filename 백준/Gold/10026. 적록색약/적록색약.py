import sys

N = int(sys.stdin.readline().strip())


picture = []
for _ in range(N):
    line = [c for c in sys.stdin.readline().strip()]
    picture.append(line)

vector = ((1, 0), (-1, 0), (0, 1), (0, -1))


def is_valid_location(x, y):
    if not 0 <= x < N:
        return False

    if not 0 <= y < N:
        return False

    return True


color_weak_visit = [[False for _ in range(N)] for _ in range(N)]
not_color_weak_visit = [[False for _ in range(N)] for _ in range(N)]


def not_color_weak(x, y):
    color = picture[y][x]
    q = [(x, y)]
    while len(q) > 0:
        x, y = q.pop()
        for xv, yv in vector:
            if is_valid_location(x + xv, y + yv) and not not_color_weak_visit[y + yv][x + xv] and color == picture[y + yv][x + xv]:
                not_color_weak_visit[y + yv][x + xv] = True
                q.append((x + xv, y + yv))


def color_weak(x, y):
    color = picture[y][x]
    if color == 'R':
        color = 'G'
    q = [(x, y)]
    while len(q) > 0:
        x, y = q.pop()
        for xv, yv in vector:
            if is_valid_location(x + xv, y + yv) and not color_weak_visit[y + yv][x + xv]:
                pixel = picture[y + yv][x + xv]
                if pixel == 'R':
                    pixel = 'G'
                if color == pixel:
                    color_weak_visit[y + yv][x + xv] = True
                    q.append((x + xv, y + yv))


color_weak_group = 0
not_color_weak_group = 0
for y in range(N):
    for x in range(N):
        if not not_color_weak_visit[y][x]:
            not_color_weak(x, y)
            not_color_weak_group += 1

        if not color_weak_visit[y][x]:
            color_weak(x, y)
            color_weak_group += 1

print(not_color_weak_group, color_weak_group)
