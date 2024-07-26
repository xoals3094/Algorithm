import sys
MAX = 100_000
N, K = map(int, sys.stdin.readline().strip().split())

visit = [False for _ in range(MAX + 1)]


def run():
    q = [N]
    visit[N] = True
    depth = 0

    while True:
        if K in q:
            return depth

        temp = []
        for x in q:
            if x - 1 >= 0 and not visit[x - 1]:
                temp.append(x-1)
                visit[x - 1] = True
            if x + 1 <= MAX and not visit[x + 1]:
                temp.append(x+1)
                visit[x + 1] = True
            if x * 2 <= MAX and not visit[x * 2]:
                temp.append(x*2)
                visit[x * 2] = True

        q = temp
        depth += 1

print(run())
