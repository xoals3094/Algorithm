import sys

N = int(sys.stdin.readline().strip())
points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

def area(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    return 0.5 * (x2 * y3 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 - x2 * y1)

total = 0
for x in range(2, N):
    total += area(points[0], points[x- 1], points[x])

print(int(abs(total * 10) + 0.5) / 10)
