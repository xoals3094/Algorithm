import sys

N, M = map(int, sys.stdin.readline().strip().split())
parents = [x for x in range(N)]

T = list(map(int, sys.stdin.readline().strip().split()))
people_of_knows_truth = []
if T[0] > 0:
    people_of_knows_truth = [
        x - 1
        for x in T[1:]
    ]


def find(n):
    while n != parents[n]:
        n = parents[n]

    return n


groups = []
for _ in range(M):
    members = [
        x - 1
        for x in list(map(int, sys.stdin.readline().strip().split()))[1:]
    ]
    for member in members:
        root = find(members[0])
        parents[find(member)] = root

    groups.append(members)


truth_group = {}
for person_of_knows_truth in people_of_knows_truth:
    root = find(person_of_knows_truth)
    truth_group[root] = True

count = M
for members in groups:
    for member in members:
        root = find(member)
        if root in truth_group:
            count -= 1
            break

print(count)