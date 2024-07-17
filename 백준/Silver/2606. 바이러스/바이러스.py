import sys


C = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

network = [[] for _ in range(C)]
is_visit = [False for _ in range(C)]

for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    if end-1 not in network[start - 1]:
        network[start - 1].append(end - 1)

    if start-1 not in network[end - 1]:
        network[end - 1].append(start - 1)


def visit(c):
    if is_visit[c]:
        return

    is_visit[c] = True
    for n in network[c]:
        visit(n)


if C > 0:
    visit(0)
    count = 0
    for v in is_visit:
        if v:
            count += 1

    print(count - 1)

else:
    print(0)
