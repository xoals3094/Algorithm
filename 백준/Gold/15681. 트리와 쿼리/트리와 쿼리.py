import sys
sys.setrecursionlimit(10**6)

N, R, Q = map(int, sys.stdin.readline().strip().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)

q = [R]
while q:
    node = q.pop()
    for next in tree[node]:
        tree[next].remove(node)
        q.append(next)

subtree_count = [-1 for _ in range(N + 1)]
def count(node):
    if subtree_count[node] != -1:
        return subtree_count[node]

    total = len(tree[node])
    for next in tree[node]:
        total += count(next)

    subtree_count[node] = total
    return total

for _ in range(Q):
    r = int(sys.stdin.readline().strip())
    print(count(r) + 1)