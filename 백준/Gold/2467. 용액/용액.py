import sys

N = int(sys.stdin.readline().strip())
solutions = list(map(int, sys.stdin.readline().strip().split()))

i = 0
j = N - 1
mixed = abs(solutions[i] + solutions[j])
a = solutions[i]
b = solutions[j]

while i != j and mixed != 0:
    if abs(solutions[i] + solutions[j]) < mixed:
        mixed = abs(solutions[i] + solutions[j])
        a = solutions[i]
        b = solutions[j]

    if solutions[i] + solutions[j] > 0:
        j -= 1

    elif solutions[i] + solutions[j] < 0:
        i += 1

print(a, b)