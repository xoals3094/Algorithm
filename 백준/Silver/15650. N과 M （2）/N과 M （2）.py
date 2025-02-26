import sys

N, M = map(int, sys.stdin.readline().strip().split())

output = []


def bt(n, p):
    if len(p) == M:
        output.append(p)
        return

    for x in range(n, N + 1):
        if N - x < M - (len(p) + 1):
            return
        bt(x + 1, p + str(x))


def result():
    for x in range(1, N + 1):
        bt(x + 1, str(x))

    for p in output:
        print(' '.join(list(p)))

result()