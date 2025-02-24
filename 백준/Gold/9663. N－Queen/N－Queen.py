import sys

N = int(sys.stdin.readline().strip())
count = 0

board = [0 for _ in range(N)]

def promising(y):
    for i in range(y):
        if board[i] == board[y] or abs(i - y) == abs(board[i] - board[y]):
            return False

    return True

def bt(y):
    global count

    if y == N:
        count += 1
        return

    for x in range(N):
        board[y] = x
        if promising(y):
            bt(y + 1)
bt(0)
print(count)