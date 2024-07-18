import sys

T = int(sys.stdin.readline().strip())


def is_valid_location(x, y):

    return not ((x < 0 or x > M - 1) or (y < 0 or y > N - 1))


def get_visitable(x, y):
    can_move = []
    for location in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
        x, y = location
        if is_valid_location(x, y) and not visit[y][x] and farm[y][x]:
            can_move.append(location)

    return can_move


def baechu_insect(x, y):
    if visit[y][x] or not farm[y][x]:
        return 0

    q = [(x, y)]
    while len(q) != 0:
        x, y = q.pop()

        visit[y][x] = True

        q += get_visitable(x, y)

    return 1


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[y][x] = 1

    count = 0
    for y in range(N):
        for x in range(M):
            count += baechu_insect(x, y)

    print(count)
