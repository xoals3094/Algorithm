import sys

N = int(sys.stdin.readline().strip())

tree = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)


visited = [False for _ in range(N + 1)]

def dfs(start):
    visited[start] = True
    stack = [start]
    while stack:
        p_node = stack.pop()
        for child_node in tree[p_node]:
            if not visited[child_node]:
                parent[child_node] = p_node
                stack.append(child_node)
                visited[child_node] = True
dfs(1)
for node in range(2, N + 1):
    print(parent[node])