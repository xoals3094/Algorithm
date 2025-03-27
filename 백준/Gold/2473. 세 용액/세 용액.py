import sys

INF = 1e30

N = int(sys.stdin.readline().strip())
solutions = list(map(int, sys.stdin.readline().strip().split()))

solutions.sort()

A = 0
B = 0
C = 0
result = INF

def two_pointers(c):
    global A, B, C, result
    start = 0 if c != 0 else 1
    end = len(solutions) - 1 if c != len(solutions) - 1 else len(solutions) - 2
    while start != end:
        mixed = solutions[c] + solutions[start] + solutions[end]
        if abs(mixed) < abs(result):
            A, B, C, result = start, end, c, mixed

        if mixed < 0:
            start += 1
            if start == c:
                start += 1
        elif mixed > 0:
            end -= 1
            if end == c:
                end -= 1
        elif mixed == 0:
            return

for i in range(len(solutions)):
    two_pointers(i)

result = [solutions[A], solutions[B], solutions[C]]
result.sort()
print(' '.join(map(str, result)))
