import sys
from collections import deque


T = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split()))


sum_a = [0]
sum_b = [0]

total = 0
for a in A:
    total += a
    sum_a.append(total)

total = 0
for b in B:
    total += b
    sum_b.append(total)

count_a = {}
for end in range(1, len(sum_a)):
    for start in range(end):
        if sum_a[end] - sum_a[start] in count_a:
            count_a[sum_a[end] - sum_a[start]] += 1
        else:
            count_a[sum_a[end] - sum_a[start]] = 1


count_b = {}
for end in range(1, len(sum_b)):
    for start in range(end):
        if sum_b[end] - sum_b[start] in count_b:
            count_b[sum_b[end] - sum_b[start]] += 1
        else:
            count_b[sum_b[end] - sum_b[start]] = 1

count = 0
for a in count_a.keys():
    b = T - a
    if b in count_b:
        count += count_a[a] * count_b[b]

print(count)