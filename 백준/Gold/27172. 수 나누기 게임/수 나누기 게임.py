import sys

MAX = 1_000_000

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
flags = [False for _ in range(MAX + 1)]
for n in numbers:
    flags[n] = True

score = [0 for _ in range(MAX + 1)]

def calculate_factor(n):
    _factor = []
    i = 1
    while i * i<= n:
        if n % i * i == 0:
            _factor.append(i)
        i += 1

    factor = _factor.copy()
    for i in _factor:
        factor.append(n // i)

    factor = list(set(factor))
    return factor


for n in numbers:
    for factor in calculate_factor(n):
        if flags[factor] and factor != n:
            score[factor] += 1
            score[n] -= 1

for n in numbers:
    print(score[n], end=' ')
