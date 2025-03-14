import sys

BORD = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]

zero = []
for i in range(9):
    for j in range(9):
        if BORD[i][j] == 0:
            zero.append((j, i))

def promising(x, y, n):
    for i in range(9):
        if BORD[y][i] == n:
            return False
        if BORD[i][x] == n:
            return False

    area_x = (x // 3) * 3
    area_y =  (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if BORD[i + area_y][j + area_x] == n:
                return False

    return True

def bt(idx):
    if idx == len(zero):
        for row in BORD:
            print(*row, sep='')
        exit(0)

    x, y = zero[idx]
    for n in range(1, 9 + 1):
        if promising(x, y, n):
            BORD[y][x] = n
            bt(idx + 1)
            BORD[y][x] = 0

bt(0)

