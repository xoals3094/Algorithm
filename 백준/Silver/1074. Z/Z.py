import sys

N, r, c= map(int, sys.stdin.readline().strip().split())


def get_quadrant(x, y, n):
    n = (2 ** n / 2)
    if (x // n) == 0 and (y // n) == 0:
        return 0
    elif (x // n) == 1 and (y // n) == 0:
        return 1
    elif (x // n) == 0 and (y // n) == 1:
        return 2
    elif (x // n) == 1 and (y // n) == 1:
        return 3


def get_zero_coor(q, n):
    n = (2 ** n / 2)
    if q == 0:
        return 0, 0

    elif q == 1:
        return n, 0

    elif q == 2:
        return 0, n

    elif q == 3:
        return n, n


def z(x, y, n):
    q = get_quadrant(x, y, n)
    if n == 1:
        return q
    start_x, start_y = get_zero_coor(q, n)
    return q * 2**(n-1) * 2**(n-1) + z(x - start_x, y - start_y, n - 1)

print(z(c, r, N))
