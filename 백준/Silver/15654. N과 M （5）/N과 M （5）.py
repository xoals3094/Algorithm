import sys


N, M = map(int, sys.stdin.readline().strip().split())

numbers = list(map(int, sys.stdin.readline().strip().split()))

output = []


def bt(seq):
    if len(seq) == M:
        output.append(seq)
        return

    for i in range(N):
        if numbers[i] not in seq:
            bt(seq + [numbers[i]])

for x in range(N):
    bt([numbers[x]])

output.sort()
for o in output:
    print(' '.join(map(str, o)))