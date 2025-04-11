import sys

KID = 0
CANDY = 1

N, M, K = map(int, sys.stdin.readline().strip().split())

parents = [i for i in range(N)]
groups = [[1, c] for c in list(map(int, sys.stdin.readline().strip().split()))]

def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        groups[a][KID] += groups[b][KID]
        groups[a][CANDY] += groups[b][CANDY]
        parents[b] = a

    elif a > b:
        groups[b][KID] += groups[a][KID]
        groups[b][CANDY] += groups[a][CANDY]
        parents[a] = b

for _ in range(M):
    A, B = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())
    union(A, B)

p = set()
for parent in parents:
    p.add(find(parent))

parents = p
dp = [[0 for _ in range(K + 1)] for _ in range(len(parents) + 1)]
for i, parent in enumerate(parents):
    i += 1
    kid, candy = groups[parent]
    for k in range(K + 1):
        if k >= kid:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - kid] + candy)
        else:
            dp[i][k] = dp[i - 1][k]

print(dp[len(parents)][K - 1])