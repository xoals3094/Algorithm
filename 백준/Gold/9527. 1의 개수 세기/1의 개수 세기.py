import sys

A, B = map(int, sys.stdin.readline().split())

def bit_count(x):
    n = 0
    while x > 0:
        n += 1
        x = x >> 1

    return n

def counting(x):
    bit = bit_count(x) - 1
    result = 0
    cnt = 0
    for n in range(bit, -1, -1):
        if x & (1 << n):
            result += 2**n * n // 2 + 1 + (2**(n + 1) - 2**n) * cnt
            cnt += 1

    return result


print(counting(B) - counting(A - 1))
