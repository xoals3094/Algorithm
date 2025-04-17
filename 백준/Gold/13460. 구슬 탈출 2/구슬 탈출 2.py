import sys

FAIL = 0
SUCCESS = 1
NOTHING = 2

result = 11
N, M = 0, 0

def move(board):
    move_result = NOTHING
    for y in range(1, len(board) - 1):
        x = 1
        while x < len(board[y]) - 1:
            if board[y][x] == 'R' or board[y][x] == 'B':
                ball = board[y][x]
                board[y][x] = '.'
                for i in range(x - 1, -1, -1):
                    if board[y][i] == '#':
                        board[y][i + 1] = ball
                        break

                    elif board[y][i] == 'O':
                        if ball ==  'R':
                            move_result = SUCCESS
                        else:
                            return FAIL
                        break

                    elif board[y][i] == 'R' or board[y][i] == 'B':
                        board[y][i + 1] = ball
                        break
            x += 1

    return move_result


def rotate(arr):
    list_of_tuples = zip(*arr[::-1])
    return [list(e) for e in list_of_tuples]

def bt(board, n):
    global result

    move_result = move(board)
    if move_result == SUCCESS:
        result = min(result, n)
        return
    elif move_result == FAIL:
        return

    if n == 10:
        return

    rotated_boards = [board]
    for _ in range(3):
        board = rotate(board)
        rotated_boards.append(board)

    for rotated_board in rotated_boards:
        bt(rotated_board, n + 1)


def solution():
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

    rotated_boards = [board]
    for _ in range(3):
        board = rotate(board)
        rotated_boards.append(board)

    for rotated_board in rotated_boards:
        bt(rotated_board, 1)

    print(result if result != 11 else -1)

solution()
