import sys


N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
MAX = max(numbers)
flags = [False for _ in range(MAX + 1)]
for n in numbers:
    flags[n] = True

score = [0 for _ in range(MAX + 1)]

for n in numbers:
    i = 2
    while n * i <= MAX:
        if flags[n * i]:
            score[n] += 1
            score[n * i] -= 1
        i += 1

for n in numbers:
    print(score[n], end=' ')
