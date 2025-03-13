import sys
INF = 10e20

N, S = map(int, sys.stdin.readline().strip().split())
sequence = list(map(int, sys.stdin.readline().strip().split()))

def pointers():
    start = 0
    end = 0
    total = sequence[0]
    min_length = 0 if total >= S else INF
    while end != N - 1:
        if total >= S:
            min_length = min(min_length, end - start)
            total -= sequence[start]
            start += 1

        elif total < S or start == end:
            end += 1
            total += sequence[end]

    while start != N:
        if total >= S:
            min_length = min(min_length, end - start)
        total -= sequence[start]
        start += 1


    return min_length + 1 if min_length < INF else 0

print(pointers())

