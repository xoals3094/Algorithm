import sys


N, M = map(int, sys.stdin.readline().strip().split())

numbers = list(map(int, sys.stdin.readline().strip().split()))

output = []


def bt(index):
    if len(index) == M:
        output.append(' '.join(list(map(lambda x: str(numbers[x]), index))))
        return

    for i in range(N):
        if i not in index:
            bt(index + [i])

for x in range(N):
    bt([x])

output = list(set(output))
output = [list(map(int, o.split())) for o in output]
output.sort()
output = [' '.join(map(str, o)) for o in output]
for o in output:
    print(o)