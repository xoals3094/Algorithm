import sys


def get_gcd(a, b):
    rest = a % b
    while rest != 0 and rest != 1:
        a = b
        b = rest

        rest = a % b

    if rest == 1:
        return 1

    return b



def get_result():
    M, N, x, y = map(int, sys.stdin.readline().strip().split())
    doomsday = int(M * N / get_gcd(max(M, N), min(M, N)))
    visited = {}

    k = 0
    while doomsday > M * k:
        visited[(M * k + x)] = True
        k += 1

    k = 0
    while doomsday > N * k:
        if (N * k + y) in visited:
            return N * k + y
        k += 1

    return -1

T = int(sys.stdin.readline())
for _ in range(T):
    print(get_result())

