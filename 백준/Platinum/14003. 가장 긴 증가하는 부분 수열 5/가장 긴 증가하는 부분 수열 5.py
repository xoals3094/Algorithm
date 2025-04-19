import sys

N = int(sys.stdin.readline())
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


def solution():
    subseq = [SEQUENCE[0]]
    lis_idx = [0]
    for a in SEQUENCE[1:]:
        if subseq[-1] < a:
            subseq.append(a)
            lis_idx.append(len(subseq) - 1)
        else:
            idx = binary_search(subseq, a)
            subseq[idx] = a
            lis_idx.append(idx)

    end_idx = 0
    for i in range(len(lis_idx)):
        if lis_idx[i] == len(subseq) - 1:
            end_idx = i
            break

    answer = [end_idx]
    for idx in range(end_idx - 1, -1, -1):
        if lis_idx[idx] == lis_idx[answer[-1]] - 1:
            answer.append(idx)

    answer.reverse()

    print(len(answer))
    for idx in answer:
        print(SEQUENCE[idx], end=' ')

solution()