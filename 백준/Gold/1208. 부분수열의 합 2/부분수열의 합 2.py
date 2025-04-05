import sys
from collections import defaultdict
from itertools import combinations


N, S = map(int, sys.stdin.readline().rstrip().split())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))


def meet_in_the_middle():
    middle = N // 2
    left_sum_dict = defaultdict(int)
    right_sum_dict = defaultdict(int)
    left = sequence[:middle]
    right = sequence[middle:]
    for n in range(len(left) + 1):
        for combination in combinations(left, n):
            left_sum_dict[sum(combination)] += 1

    for n in range(len(right) + 1):
        for combination in combinations(right, n):
            right_sum_dict[sum(combination)] += 1

    cnt = 0
    for key, value in left_sum_dict.items():
        if right_sum_dict[S - key]:
            cnt += value * right_sum_dict[S - key]
    return cnt - 1 if S == 0 else cnt

print(meet_in_the_middle())
