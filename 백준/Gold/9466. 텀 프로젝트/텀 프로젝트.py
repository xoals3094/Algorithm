import sys
sys.setrecursionlimit(10**5)

T = int(sys.stdin.readline().strip())


def dfs(current):
    global count

    next = select[current]
    visited[current] = True
    if not visited[next]:
        dfs(next)

    else:
        if not finished[next]:
            count -= 1
            while next != current:
                count -= 1
                next = select[next]

    finished[current] = True


for _ in range(T):
    count = int(sys.stdin.readline().strip())
    select = list(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split()))
    visited = [False for _ in range(count)]
    finished = [False for _ in range(count)]
    for i in range(count):
        if not visited[i]:
            dfs(i)
    print(count)

