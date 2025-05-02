import sys

T = int(sys.stdin.readline().rstrip())


def F(n):
    reverse = ''
    for x in n:
        reverse += str(9 - int(x))

    return reverse


for _ in range(T):
    N = list(sys.stdin.readline().rstrip())
    if N[0] >= '5':
        N[0] = '5'
        for i in range(1, len(N)):
            N[i] = '0'

    print(int(''.join(N)) * int(F(N)))
