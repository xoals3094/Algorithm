import sys

N, M = map(int, sys.stdin.readline().strip().split())

trees = [int(x) for x in sys.stdin.readline().strip().split()]


def cutting(height):
    total = 0
    for tree in trees:
        rest = tree - height
        if rest > 0:
            total += rest

    return total


def search(start, end):
    while start + 1 != end:
        mid = int((start + end) / 2)
        total = cutting(mid)
        if total == M:
            return mid
        elif total > M:
            start = mid
        elif total < M:
            end = mid

    return start


print(search(0, max(trees)))
