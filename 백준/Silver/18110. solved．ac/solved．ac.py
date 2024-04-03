import sys
input = sys.stdin.readline


def my_round(f):
    return int(f + 0.5)


n = int(input())

result = 0
if n != 0:
    levels = []
    for _ in range(n):
        level = int(input())
        levels.append(level)

    levels.sort()

    r = my_round(n * 0.15)

    if r != 0:
        levels = levels[r:-r]

    result = my_round(sum(levels) / len(levels))
print(result)

