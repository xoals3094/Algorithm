import sys
from collections import deque

NONE = 0
RED = 1
BLUE = -1

K = int(sys.stdin.readline())

def get_none(visited):
    for i in range(len(visited)):
        if visited[i] == NONE:
            return i

    return -1

def bfs(start, visited, graph):
    q = deque([start])
    visited[start] = RED
    while q:
        node = q.popleft()
        color = visited[node]
        for next in graph[node]:
            if visited[next] == NONE:
                visited[next] = color * -1
                q.append(next)
            elif visited[next] == color:
                return False

    return True

def bipartite_graph():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    visited = [NONE for _ in range(v)]
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    i = get_none(visited)
    while i != -1:
        if not bfs(i, visited, graph):
            return "NO"
        i = get_none(visited)

    return "YES"

for _ in range(K):
    print(bipartite_graph())