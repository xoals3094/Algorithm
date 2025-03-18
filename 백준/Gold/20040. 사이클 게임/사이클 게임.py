import sys

N, M = map(int, sys.stdin.readline().strip().split())
turn = 0
parents = [x for x in range(N)]

def find(x):
    parent = parents[x]
    while parent != parents[parent]:
        parent = parents[parent]

    return parent

def union(a, b):
    a = find(a)
    b = find(b)
    if a <= b:
        parents[b] = a
    else:
        parents[a] = b


def go(a, b):
    global turn
    turn += 1
    if find(a) == find(b):
        return turn

    union(a, b)
    return 0

def cycle_game():
    result = 0
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        result = go(a, b)
        if result > 0 :
            return result
    return result

print(cycle_game())

