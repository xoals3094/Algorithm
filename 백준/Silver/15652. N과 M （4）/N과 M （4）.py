import sys

N, M = map(int, sys.stdin.readline().strip().split())

output = []

def bt(n, p):
    if len(p) == M:
        output.append(' '.join(list(map(str, p))))
        return

    for x in range(n, N + 1):
        bt(x, p + [x])

bt(1, [])

for o in output:
    print(o)
