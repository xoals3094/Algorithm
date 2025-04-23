import sys

N = int(sys.stdin.readline())
board = [sys.stdin.readline().rstrip().split() for _ in range(N)]


def promise(x, y):
    # left
    i = 0
    while y - i != -1 and x - i != -1:
        if board[y - i][x - i] == 'B':
            return False
        i += 1

    # right
    i = 0
    while y - i != -1 and x + i != N:
        if board[y - i][x + i] == 'B':
            return False
        i += 1

    return True


def get_space(h):
    space = []
    if h < N:
        x = 0
        y = h
    else:
        x = h - (N - 1)
        y = (N - 1)

    i = 0
    while y - i != -1 and x + i != N:
        if board[y - i][x + i] == '1':
            space.append((x + i, y - i))
        i += 1

    return space


spaces = [get_space(i) for i in range(N * 2 - 1)]
def bt(h, n, count):
    if h > N * 2 - 2:
        return max(count, n)

    # 놓는 선택
    for x, y in spaces[h]:
        if promise(x, y):
            board[y][x] = 'B'
            count = bt(h + 2, n + 1, count)
            board[y][x] = '1'
    count = bt(h + 2, n, count) # 놓지 않는 선택
    return count


def solution():
    total = bt(0, 0, 0) + bt(1, 0, 0)
    return total

print(solution())
