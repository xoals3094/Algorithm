import sys
import math

N = int(sys.stdin.readline().strip())

sizes = list(map(int, list(sys.stdin.readline().strip().split())))

T, P = list(map(int, list(sys.stdin.readline().strip().split())))

t_total = 0
for size in sizes:
    t_total += math.ceil(size / T)

p_bundle = int(N / P)
p_piece = N % P

print(t_total)
print(p_bundle, p_piece)
