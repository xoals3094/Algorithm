import sys

N, K = map(int, sys.stdin.readline().split())

groups = []
for _ in range(K):
    group = (list(map(int, sys.stdin.readline().split()))[1:])
    group.sort()
    groups.append(group)


for group in groups:
    for i in range(len(group)):
        print(group[i] + i + 1, end=' ')
    print()
