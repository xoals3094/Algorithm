import sys
from typing import List

N = int(sys.stdin.readline().strip())
_map = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]


def is_valid_location(x, y):
    if not 0 <= x < N:
        return False

    if not 0 <= y < N:
        return False

    if visit[y][x]:
        return False

    if _map[y][x] == 0:
        return False

    return True


def find_complex(x, y):
    q = [(x, y)]
    count = 0
    while len(q) > 0:
        x, y = q.pop()
        count += 1
        if is_valid_location(x - 1, y):
            visit[y][x - 1] = True
            q.append((x - 1, y))

        if is_valid_location(x + 1, y):
            visit[y][x + 1] = True
            q.append((x + 1, y))

        if is_valid_location(x, y - 1):
            visit[y - 1][x] = True
            q.append((x, y - 1))

        if is_valid_location(x, y + 1):
            visit[y + 1][x] = True
            q.append((x, y + 1))

    return count


def main():
    apartment_complex = []
    for y in range(N):
        for x in range(N):
            if _map[y][x] == 1 and not visit[y][x]:
                visit[y][x] = True
                count = find_complex(x, y)
                apartment_complex.append(count)

    apartment_complex.sort()
    print(len(apartment_complex))
    for count in apartment_complex:
        print(count)


main()
