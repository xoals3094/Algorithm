import sys
INF = int(10e7)

LEFT = 0
RIGHT = 1

MAX = 10_000

graph = [[-1, -1] for _ in range(MAX + 1)]
values = [INF for _ in range(MAX)]

def insert_node(v, node):
    next = 0
    while True:
        if v < values[next]:
            if graph[next][LEFT] == -1:
                graph[next][LEFT] = node
                break
            next = graph[next][LEFT]
        else:
            if graph[next][RIGHT] == -1:
                graph[next][RIGHT] = node
                break
            next = graph[next][RIGHT]


def init():
    root = int(sys.stdin.readline())
    values[0] = root

    node = 1
    while True:
        v = sys.stdin.readline()
        if v == '':
            break

        v = int(v)
        values[node] = v
        insert_node(v, node)
        node += 1



def postorder():
    visited = [False for _ in range(MAX)]

    stack = [0]
    while stack:
        top = stack[-1]
        left, right = graph[top]
        if  (left == -1 or visited[left]) and (right == -1 or visited[right]):
            print(values[stack.pop()])

        if not visited[right] and right != -1:
            stack.append(right)
            visited[right] = True

        if not visited[left] and left != -1:
            stack.append(left)
            visited[left] = True


init()
postorder()