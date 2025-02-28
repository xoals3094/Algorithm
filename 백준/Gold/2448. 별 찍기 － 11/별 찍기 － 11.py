import sys


N = int(sys.stdin.readline().strip())

graph = [
    [' ', ' ', '*', ' ', ' '],
    [' ', '*', ' ', '*', ' '],
    ['*', '*', '*', '*', '*']
]


def star(n, before):
    if n >= N:
        return before

    after = [
        [' ' for _ in range(n * 4 - 1)]
        for  _ in range(n * 2)
    ]

    for y in range(n):
        for i, c in enumerate(before[y]):
            after[y][i + n] = c

    for y in range(n):
        for i, c in enumerate(before[y]):
            after[y + n][i] = c

    for y in range(n):
        for i, c in enumerate(before[y]):
            after[y + n][i + n * 2] = c

    return star(n * 2, after)

graph = star(3, graph)

for line in graph:
    print(''.join(line))

