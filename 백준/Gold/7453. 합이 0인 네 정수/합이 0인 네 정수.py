import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
ABCD = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

A, B, C, D = 0, 1, 2, 3

left_sum = defaultdict(int)
for i in range(N):
    for j in range(N):
        left_sum[ABCD[i][A] + ABCD[j][B]] += 1

cnt = 0
for i in range(N):
    for j in range(N):
        tmp = -(ABCD[i][C] + ABCD[j][D])
        if tmp in left_sum.keys():
            cnt += left_sum[tmp]

print(cnt)
