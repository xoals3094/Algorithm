import sys
from collections import deque

VECTOR = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
)

graph = []
T = int(sys.stdin.readline())
H, W = 0, 0

def key_to_number(key):
    return ord(key) - ord('a')

def door_to_number(door):
    return ord(door) - ord('A')


def is_door(c):
    return ord('A') <= ord(c) <= ord('Z')

def is_key(c):
    return ord('a') <= ord(c) <= ord('z')


def is_valid(x, y):
    return 0 <= x < W and 0 <= y < H



def bfs(keys):
    visited = [[False for _ in range(W)] for _ in range(H)]
    locked_door = [[] for _ in range(26)] # 잠긴 문 위치

    q = deque()
    documents = 0
    for y in [0, H - 1]:
        for x in range(W):
            if visited[y][x]:
                continue

            if graph[y][x] == '.':
                q.append((x, y))
                visited[y][x] = True

            elif graph[y][x] == '$':
                documents += 1
                q.append((x, y))
                visited[y][x] = True

            elif is_door(graph[y][x]):
                door = door_to_number(graph[y][x])
                if keys & 1 << door:  # 키 있음
                    visited[y][x] = True
                    q.appendleft((x, y))
                else:
                    locked_door[door].append((x, y))

            elif is_key(graph[y][x]):
                key = key_to_number(graph[y][x])
                keys = keys | 1 << key
                visited[y][x] = True
                q.appendleft((x, y))
                for mx, my in locked_door[key]:
                    visited[my][mx] = True
                    q.appendleft((mx, my))


    for y in range(H):
        for x in [0, W - 1]:
            if visited[y][x]:
                continue

            if graph[y][x] == '.':
                q.append((x, y))
                visited[y][x] = True

            elif graph[y][x] == '$':
                documents += 1
                q.append((x, y))
                visited[y][x] = True

            elif is_door(graph[y][x]):
                door = door_to_number(graph[y][x])
                if keys & 1 << door:  # 키 있음
                    visited[y][x] = True
                    q.appendleft((x, y))
                else:
                    locked_door[door].append((x, y))

            elif is_key(graph[y][x]):
                key = key_to_number(graph[y][x])
                keys = keys | 1 << key
                visited[y][x] = True
                q.appendleft((x, y))
                for mx, my in locked_door[key]:
                    visited[my][mx] = True
                    q.appendleft((mx, my))

    while q:
        x, y = q.popleft()
        for vx, vy in VECTOR:
            mx, my = x + vx, y + vy
            if is_valid(mx, my) and not visited[my][mx] and graph[my][mx] != '*':
                if graph[my][mx] == '$':
                    documents += 1
                    q.append((mx, my))
                    visited[my][mx] = True

                elif is_door(graph[my][mx]):
                    door = door_to_number(graph[my][mx])
                    if keys & 1 << door: # 키 있음
                        visited[my][mx] = True
                        q.appendleft((mx, my))
                    else:
                        locked_door[door].append((mx, my))

                elif is_key(graph[my][mx]):
                    key = key_to_number(graph[my][mx])
                    keys = keys | 1 << key
                    visited[my][mx] = True
                    q.appendleft((mx, my))
                    for mx, my in locked_door[key]:
                        visited[my][mx] = True
                        q.appendleft((mx, my))

                else:
                    visited[my][mx] = True
                    q.appendleft((mx, my))


    return documents


def solution():
    global H, W, graph
    H, W = map(int, sys.stdin.readline().rstrip().split())
    graph = [sys.stdin.readline().rstrip() for _ in range(H)]
    key_string = sys.stdin.readline().rstrip()
    keys = 0
    if key_string != "0":
        for key in key_string:
            keys = keys | 1 << key_to_number(key)

    return bfs(keys)


for _ in range(T):
    print(solution())

