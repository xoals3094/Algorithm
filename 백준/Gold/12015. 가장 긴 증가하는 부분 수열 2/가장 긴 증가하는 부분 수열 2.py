import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
LIS = [A[0]]

def search_index(n):
    start = 0
    end = len(LIS) - 1
    while start <= end:
        mid = (start + end) // 2
        if n > LIS[mid]:
            start = mid + 1
        elif n < LIS[mid]:
            end = mid - 1
        else:
            return mid

    return start

for x in A[1:]:
    if x > LIS[-1]:
        LIS.append(x)
    else:
        i = search_index(x)
        LIS[i] = x
print(len(LIS))
