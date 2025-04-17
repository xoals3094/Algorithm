import sys
from collections import deque


VECTOR = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
)

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)] # visited[ry][rx][by][bx]

def move(rx, ry, bx, by, vx, vy):
    m_rx, m_ry, m_bx, m_by = rx, ry, bx, by

    while board[m_ry][m_rx] != '#' and board[m_ry][m_rx] != 'O':
        m_rx += vx
        m_ry += vy

    if board[m_ry][m_rx] == '#':
        m_rx -= vx
        m_ry -= vy

    while board[m_by][m_bx] != '#' and board[m_by][m_bx] != 'O':
        m_bx += vx
        m_by += vy

    if board[m_by][m_bx] == '#':
        m_bx -= vx
        m_by -= vy

    if m_rx == m_bx and m_ry == m_by:
        if board[m_ry][m_rx] == 'O':
            return m_rx, m_ry, m_bx, m_by

        if vx == -1:
            return (m_rx, m_ry, m_bx - vx, m_by) if rx < bx else (m_rx - vx, m_ry, m_bx, m_by)

        elif vx == 1:
            return (m_rx, m_ry, m_bx - vx, m_by) if rx > bx else (m_rx - vx, m_ry, m_bx , m_by)

        elif vy == -1:
            return (m_rx, m_ry, m_bx, m_by - vy) if ry < by else (m_rx, m_ry - vy, m_bx, m_by)

        elif vy == 1:
            return (m_rx, m_ry, m_bx, m_by - vy) if ry > by else (m_rx, m_ry - vy, m_bx, m_by)

    return m_rx, m_ry, m_bx, m_by



def bfs(rx, ry, bx, by):
    q = deque([(rx, ry, bx, by, 0)])
    visited[ry][rx][by][bx] = True
    while q:
        rx, ry, bx, by, n = q.popleft()
        for vx, vy in VECTOR:
            m_rx, m_ry, m_bx, m_by = move(rx, ry, bx, by, vx, vy)
            if visited[m_ry][m_rx][m_by][m_bx]:
                continue

            if board[m_ry][m_rx] == 'O' and board[m_by][m_bx] == 'O':
                continue

            elif board[m_ry][m_rx] == 'O':
                return n + 1

            else:
                if n + 1 < 10:
                    q.append((m_rx, m_ry, m_bx, m_by, n + 1))
                    visited[m_ry][m_rx][m_by][m_bx] = True

    return -1

def solution():
    rx, ry, bx, by = 0, 0, 0, 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'R':
                rx, ry = x, y
            elif board[y][x] == 'B':
                bx, by = x, y

    board[ry][rx] = '.'
    board[by][bx] = '.'

    print(bfs(rx, ry, bx, by))

solution()