import sys

A = int(sys.stdin.readline())
SEQUENCE = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(subseq, a) -> int:
    start, end = 0, len(subseq) - 1
    while start <= end:
        mid = (start + end) // 2
        if a > subseq[mid]:
            start = mid + 1
        elif a < subseq[mid]:
            end = mid - 1
        else:
            return mid

    return start


def insert(subseq, a):
    idx = binary_search(subseq, a)
    subseq[idx] = a

def solution():
    subseq = [SEQUENCE[0]]
    for a in SEQUENCE[1:]:
        if subseq[-1] < a:
            subseq.append(a)
        else:
            insert(subseq, a)

    print(len(subseq))
solution()