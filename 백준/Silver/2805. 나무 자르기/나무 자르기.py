import sys

N, M = map(int, sys.stdin.readline().strip().split())

trees = [int(x) for x in sys.stdin.readline().strip().split()]
total_cache = {}


def cutting(height):
    try:
        total = total_cache[height]
    except Exception:
        total = 0
        for tree in trees:
            rest = tree - height
            if rest > 0:
                total += rest
        total_cache[height] = total

    return total


def search(start, end):
    mid = int((start + end) / 2)
    if start == mid:
        return start

    total = cutting(mid)
    if total == M:
        return mid

    if total >= M:
        return search(mid, end)

    if total < M:
        return search(start, mid)


print(search(0, max(trees)))
