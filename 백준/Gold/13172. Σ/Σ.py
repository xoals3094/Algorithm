import sys

M = int(sys.stdin.readline().strip())

MODULAR = 1_000_000_007


def get_inverse_element(b):
    res = 1
    n = MODULAR - 2
    while n:
        if n & 1:
            res = (res * b) % MODULAR

        b = (b * b) % MODULAR
        n //= 2

    return res

total = 0
for _ in range(M):
    N, S = map(int, sys.stdin.readline().strip().split())
    total = (total + S // N) % MODULAR  if S % N == 0 else (total + (S * get_inverse_element(N)) % MODULAR) % MODULAR

print(total)