import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

total = 0
for _ in range(n):
    a, b = map(lambda d: int(d), sys.stdin.readline().split(' '))
    total += a * b

if x == total:
    print('Yes')
else:
    print('No')
