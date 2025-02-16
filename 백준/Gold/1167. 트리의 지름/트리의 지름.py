import sys


N = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N)]
for _ in range(N):
    edge = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, len(edge) - 1, 2):
        a = edge[0] - 1
        b = edge[i] - 1
        cost = edge[i + 1]
        graph[a].append((b, cost))


def dfs(node):
    costs = [0 for _ in range(N)]
    visited = [False for _ in range(N)]
    visited[node] = True
    stack = [node]
    while len(stack) > 0:
        node = stack.pop()
        for next, cost in graph[node]:
            if visited[next] is False:
                costs[next] = costs[node] + cost
                visited[next] = True
                stack.append(next)

    node = -1
    max = 0
    for i, cost in enumerate(costs):
        if cost > max:
            node = i
            max = cost

    return node, max


node, max = dfs(0)
node, max = dfs(node)

print(max)

