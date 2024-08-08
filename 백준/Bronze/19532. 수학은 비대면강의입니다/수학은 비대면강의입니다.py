import sys

a, b, c, d, e, f = list(map(int, sys.stdin.readline().strip().split()))


def cal():
    for x in range(-999, 999 + 1):
        for y in range(-999, 999 + 1):
            exp1 = (a * x) + (b * y)
            if exp1 == c:
                exp2 = (d * x) + (e * y)
                if exp2 == f:
                    return x, y


x, y = cal()
print(x, y)
