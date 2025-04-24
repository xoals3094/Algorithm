import sys

def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    result = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
    if result < 0:
        return -1
    elif result > 0:
        return 1
    return 0

def crossing(segment_a, segment_b):
    a, b = segment_a
    c, d = segment_b

    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        a, b = (b, a) if b < a else (a, b)
        c, d = (d, c) if d < c else (c, d)

        return c <= b and a <= d

    return ab <= 0 and cd <= 0


N = int(sys.stdin.readline())
segments = []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    segments.append(((a, b), (c, d)))

parents = [x for x in range(N)]
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


for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if crossing(segments[i], segments[j]):
            if find(i) != find(j):
                union(i, j)

segment_count = [0 for _ in range(N)]
for i in range(N):
    segment_count[find(i)] += 1

print(len(set(parents)))
print(max(segment_count))

