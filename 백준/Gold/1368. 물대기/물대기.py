import sys

N = int(sys.stdin.readline())
edges = []
for n in range(1, N + 1):
    edges.append((0, n, int(sys.stdin.readline())))

for a in range(N):
    for b, p in enumerate(map(int, sys.stdin.readline().rstrip().split())):
        if a != b:
            edges.append((a + 1, b + 1, p))

edges.sort(key=lambda x: x[2])

parents = [x for x in range(N + 1)]
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    a, b = (b, a) if b < a else (a, b)
    parents[b] = a


def mst():
    total = 0
    for a, b, p in edges:
        if find(a) != find(b):
            total += p
            union(a, b)

    return total


print(mst())