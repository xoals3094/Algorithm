import sys


N, M = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()
output = {}

def bt(n, p):
    if len(p) == M:
        output[p] = True
        return

    for i in range(n, N):
        bt(i, p + (numbers[i],))

bt(0, (),)
output = list(output.keys())
for o in output:
    print(' '.join(list(map(str, o))))
