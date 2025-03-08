import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split()))

def max(start, sequence):
    value = sequence[start]
    idx = start
    i = start
    while i < len(sequence):
        if sequence[i] > value:
            value = sequence[i]
            idx = i
        i += 1
    return idx

result = []
a_idx = 0
b_idx = 0
while a_idx != len(A) and b_idx != len(B):
    a_idx = max(a_idx, A)
    b_idx = max(b_idx, B)
    if A[a_idx] == B[b_idx]:
        result.append(A[a_idx])
        A = A[a_idx + 1:]
        B = B[b_idx + 1:]
        a_idx = 0
        b_idx = 0

    elif A[a_idx] > B[b_idx]:
        A[a_idx] = 0
        a_idx = 0

    elif A[a_idx] < B[b_idx]:
        B[b_idx] = 0
        b_idx = 0

result = list(filter(lambda x: x != 0, result))
print(len(result))
print(' '.join(list(map(str, result))))
