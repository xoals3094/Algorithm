import sys
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

dock_gate = [x for x in range(G + 1)]

def find(n):
    if n == dock_gate[n]:
        return dock_gate[n]

    dock_gate[n] = find(dock_gate[n])
    return dock_gate[n]

cnt = 0
for _ in range(P):
    g = int(sys.stdin.readline())
    actual_gate = find(g)
    if actual_gate == 0:
        break
    dock_gate[g] = actual_gate
    cnt += 1

    dock_gate[actual_gate] = find(actual_gate - 1)


print(cnt)
