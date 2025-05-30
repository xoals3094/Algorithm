import sys

COOR = 0
NUMBER = 1

N = int(sys.stdin.readline())
planets = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

planet_by_x = []
planet_by_y = []
planet_by_z = []
for n, planet in enumerate(planets):
    x, y, z = planet
    planet_by_x.append((x, n))
    planet_by_y.append((y, n))
    planet_by_z.append((z, n))

planet_by_x.sort()
planet_by_y.sort()
planet_by_z.sort()

edges = []
for i in range(N - 1):
    a, b = planet_by_x[i][NUMBER], planet_by_x[i + 1][NUMBER]
    edges.append((abs(planet_by_x[i][COOR] - planet_by_x[i + 1][COOR]), a, b))

    a, b = planet_by_y[i][NUMBER], planet_by_y[i + 1][NUMBER]
    edges.append((abs(planet_by_y[i][COOR] - planet_by_y[i + 1][COOR]), a, b))

    a, b = planet_by_z[i][NUMBER], planet_by_z[i + 1][NUMBER]
    edges.append((abs(planet_by_z[i][COOR] - planet_by_z[i + 1][COOR]), a, b))

edges.sort()
parents = [x for x in range(N)]
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        a, b = b, a

    parents[b] = a

def mst():
    total = 0
    cnt = N - 1
    for d, a, b in edges:
        if cnt == 0:
            break

        if find(a) == find(b):
            continue

        union(a, b)
        cnt -= 1
        total += d

    return total

print(mst())