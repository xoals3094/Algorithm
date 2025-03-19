import sys


N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
MAX = max(numbers)
flags = [False for _ in range(MAX + 1)]
for n in numbers:
    flags[n] = True

score = [0 for _ in range(MAX + 1)]

def calculate_factor(n):
    _factor = []
    i = 1
    while i * i < n:
        if n % i * i == 0:
            _factor.append(i)
            yield i
        i += 1

    if i * i == n:
        yield i

    for i in _factor:
        yield n // i

for n in numbers:
    for factor in calculate_factor(n):
        if flags[factor] and factor != n:
            score[factor] += 1
            score[n] -= 1

for n in numbers:
    print(score[n], end=' ')
