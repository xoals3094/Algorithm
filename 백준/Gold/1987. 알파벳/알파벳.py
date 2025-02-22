import sys

R, C = map(int, sys.stdin.readline().strip().split())

grid = [sys.stdin.readline().strip() for _ in range(R)]


MOVE = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
)

output = 0
visited = [False for _ in range(26)]
def dfs(x, y, count):
    global output
    output = max(output, count)

    for move_x, move_y in MOVE:
        position_x = x + move_x
        position_y = y + move_y
        if 0 <= position_x < C and 0 <= position_y < R and not visited[ord(grid[position_y][position_x]) - 65]:
            visited[ord(grid[position_y][position_x]) - 65] = True
            dfs(position_x, position_y, count + 1)
            visited[ord(grid[position_y][position_x]) - 65] = False

visited[ord(grid[0][0]) - 65] = True
dfs(0, 0, 1)
print(output)

