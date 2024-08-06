import sys
from typing import List

N, M = map(int, sys.stdin.readline().strip().split())

friends: List[List[int]] = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)


def bfs(user):
    visit = [False for _ in range(N)]
    visit[user] = True

    depth = 1
    bacon = 0
    q = [user]
    while len(q) > 0:
        temp = []
        for user in q:
            for friend in friends[user]:
                if not visit[friend]:
                    visit[friend] = True
                    temp.append(friend)
                    bacon += depth
        q = temp

        depth += 1
    return bacon


bacons = [999999 for _ in range(N)]
min_index = 0
for x in range(N):
    bacon = bfs(x)
    if bacons[min_index] > bacon:
        min_index = x
    bacons[x] = bacon
print(min_index + 1)

