import sys

N = int(sys.stdin.readline().strip())
tang_hulu = list(map(int, sys.stdin.readline().strip().split()))


count = [0 for _ in range(9)]


def kind_of_fruits():
    kinds = 0
    for x in count:
        if x != 0:
            kinds += 1
    return kinds


def tang_tang_hulu_hulu():
    start = 0
    end = 0

    count[tang_hulu[start] - 1] = 1
    max_length = 1
    while start < N:
        kinds = kind_of_fruits()
        if kinds > 2 or end == N - 1:
            count[tang_hulu[start] - 1] -= 1
            start += 1
            max_length = max(max_length, end - start + 1)

        elif kinds <= 2:
            end += 1
            count[tang_hulu[end] - 1] += 1
            if kind_of_fruits() <= 2:
                max_length = max(max_length, end - start + 1)

    print(max_length)


tang_tang_hulu_hulu()
