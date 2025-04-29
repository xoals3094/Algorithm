import sys

K = int(sys.stdin.readline())

def solution():
    start = 0
    k = 1
    while start < K:
        start += 2 ** k
        k += 1
    start -= 2 ** (k - 1)
    x = K - start - 1
    result = []
    for _ in range(k - 1):
        if x & 1:
            result.append('7')
        else:
            result.append('4')
        x >>= 1

    result.reverse()
    print(''.join(result))

solution()
