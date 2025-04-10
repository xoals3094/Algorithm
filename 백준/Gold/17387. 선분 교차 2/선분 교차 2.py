import sys


def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    return x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)


X1, Y1, X2, Y2 = list(map(int, sys.stdin.readline().split()))
A, B = (X1, Y1), (X2, Y2)

X1, Y1, X2, Y2 = list(map(int, sys.stdin.readline().split()))
C, D = (X1, Y1), (X2, Y2)


def is_crossing():
    global A, B, C, D
    ab = ccw(A, B, C) * ccw(A, B, D)
    cd =  ccw(C, D, A) * ccw(C, D, B)
    if ab == 0 and cd == 0:
        if A > B: A, B = B, A
        if C > D: C, D = D, C

        return C <= B and A <= D

    return ab <= 0 and cd <= 0

print(int(is_crossing()))
