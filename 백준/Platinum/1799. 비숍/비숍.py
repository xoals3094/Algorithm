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

count = 0
def bt(h, n):
    global count
    if (N * 2 - 2) - h + n <= count - 1:
        return

    if h > N * 2 - 2:
        count = max(count, n)
        return

    # 놓는 선택
    for x, y in spaces[h]:
        if promise(x, y):
            board[y][x] = 'B'
            bt(h + 1, n + 1)
            board[y][x] = '1'
    bt(h + 1, n) # 놓지 않는 선택
if N != 1:
    bt(0, 0)
else:
    if board[0][0] == '1':
        count += 1

print(count)
