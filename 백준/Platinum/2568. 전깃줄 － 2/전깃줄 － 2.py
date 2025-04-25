import sys

A, B = 0, 1

N = int(sys.stdin.readline().rstrip())

using = {}
wires = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    wires.append((a, b))
    using[a] = False

wires.sort()
def search(lis, x):
    start, end = 0, len(lis) - 1
    while start <= end:
        mid = (start + end) // 2
        if x < lis[mid]:
            end = mid - 1
        elif lis[mid] < x:
            start = mid + 1
        else:
            return mid

    return start

def solution():
    lis = [wires[0][B]]
    index = [0]
    for a, b in wires[1:]:
        if lis[-1] < b:
            lis.append(b)
            i = len(lis) - 1
        else:
            i = search(lis, b)
            lis[i] = b

        index.append(i)

    m = index.index(max(index))
    using[wires[m][A]] = True
    next = index[m] - 1
    i = m - 1
    while next >= 0:
        if index[i] == next:
            using[wires[i][A]] = True
            next -= 1
        i -= 1

    result = []
    for number, used in using.items():
        if not used:
            result.append(number)

    result.sort()
    print(len(result))
    for number in result:
        print(number)

solution()
