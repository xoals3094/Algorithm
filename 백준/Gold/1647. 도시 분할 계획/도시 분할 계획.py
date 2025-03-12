import sys

N, M = map(int, sys.stdin.readline().strip().split())
edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    edges.append((c, a, b))

edges.sort()

parents = [i for i in range(N + 1)]
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(x):
    while x != parents[x]:
        x = parents[x]

    return x

def mst():
    total = 0
    count = 0
    for c, a, b in edges:
        if find(a) != find(b):
            count += 1
            if count == N - 1:
                break
            total += c
            union(a, b)

    return total

print(mst())