import sys

N, M = map(int, sys.stdin.readline().strip().split())

graph = [x for x in range(N * M)]

for i in range(N):
    for j, x in enumerate(sys.stdin.readline().strip()):
        node = i * M + j
        if x == "D":
            graph[node] = node + M
        elif x == "U":
            graph[node] = node - M
        elif x == "L":
            graph[node] = node - 1
        elif x == "R":
            graph[node] = node + 1

visited = [False for _ in range(N * M)]
def find(x):
    if x == graph[x]:
        return x

    graph[x] = find(graph[x])
    return graph[x]


def dfs(x):
    if visited[x]:
        return x

    visited[x] = True
    graph[x] = dfs(graph[x])
    return graph[x]

if N * M > 1:
    for i in range(N * M):
        if not visited[i]:
            graph[i] = dfs(i)

    for i in range(N * M):
        graph[i] = find(i)

    groups = {}
    for i in range(N * M):
        groups[graph[i]] = True
    print(len(groups))

else:
    print(1)

