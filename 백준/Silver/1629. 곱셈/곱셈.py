import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

def fpow(n, m):
    result = 1
    while m > 0:
        if m % 2 == 1:
            result = (n * result) % C
            m -= 1

        n = (n * n) % C
        m //= 2

    return result



print(fpow(A, B) % C)