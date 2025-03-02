import sys

N, B = map(int, sys.stdin.readline().strip().split())

A = [
    list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)
]


def mul_matrix(a1, a2):
    result = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]

    for y in range(N):
        for x in range(N):
            for i in range(N):
                result[y][x] = (result[y][x] + (a1[y][i] * a2[i][x]) % 1000) % 1000
    return result

def power(a, b):
    res = [
        [1 if x == y else 0 for x in range(N)]
        for y in range(N)
    ]
    while b:
        if b & 1:
            res = mul_matrix(a, res)
        a = mul_matrix(a, a)
        b //= 2

    return res


def get_result():
    result = power(A, B)
    for y in range(N):
        print(' '.join(list(map(str, result[y]))))

get_result()