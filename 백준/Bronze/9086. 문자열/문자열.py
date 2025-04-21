import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A = sys.stdin.readline().rstrip()
    print(f'{A[0]}{A[-1]}')