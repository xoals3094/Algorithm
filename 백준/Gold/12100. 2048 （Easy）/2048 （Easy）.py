import sys
import copy

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0

def move(direction, before_board, count):
    global result

    current_board = copy.deepcopy(before_board)
    if direction == UP:
        for x in range(N):
            numbers = []
            for y in range(N):
                if current_board[y][x] > 0:
                    numbers.append(current_board[y][x])
                    current_board[y][x] = 0

            i = 0
            y = 0
            while i < len(numbers) - 1:
                if numbers[i] == numbers[i + 1]:
                    current_board[y][x] = numbers[i] + numbers[i + 1]
                    i += 1
                else:
                    current_board[y][x] = numbers[i]
                y += 1
                i += 1

            if i == len(numbers) - 1:
                current_board[y][x] = numbers[i]

    elif direction == DOWN:
        for x in range(N):
            numbers = []
            for y in range(N - 1, -1, -1):
                if current_board[y][x] > 0:
                    numbers.append(current_board[y][x])
                    current_board[y][x] = 0

            i = 0
            y = N - 1
            while i < len(numbers) - 1:
                if numbers[i] == numbers[i + 1]:
                    current_board[y][x] = numbers[i] + numbers[i + 1]
                    i += 1
                else:
                    current_board[y][x] = numbers[i]

                i += 1
                y -= 1

            if i == len(numbers) - 1:
                current_board[y][x] = numbers[i]

    elif direction == LEFT:
        for y in range(N):
            numbers = []
            for x in range(N):
                if current_board[y][x] > 0:
                    numbers.append(current_board[y][x])
                    current_board[y][x] = 0

            i = 0
            x = 0
            while i < len(numbers) - 1:
                if numbers[i] == numbers[i + 1]:
                    current_board[y][x] = numbers[i] + numbers[i + 1]
                    i += 1
                else:
                    current_board[y][x] = numbers[i]

                x += 1
                i += 1

            if i == len(numbers) - 1:
                current_board[y][x] = numbers[i]

    elif direction == RIGHT:
        for y in range(N):
            numbers = []
            for x in range(N - 1, -1, -1):
                if current_board[y][x] > 0:
                    numbers.append(current_board[y][x])
                    current_board[y][x] = 0

            i = 0
            x = N - 1
            while i < len(numbers) - 1:
                if numbers[i] == numbers[i + 1]:
                    current_board[y][x] = numbers[i] + numbers[i + 1]
                    i += 1
                else:
                    current_board[y][x] = numbers[i]

                x -= 1
                i += 1

            if i == len(numbers) - 1:
                current_board[y][x] = numbers[i]

    if count == 5:
        for y in range(N):
            for x in range(N):
                result = max(result, current_board[y][x])

        return

    for next in [UP, DOWN, LEFT, RIGHT]:
        move(next, current_board, count + 1)

for next in [UP, DOWN, LEFT, RIGHT]:
    move(next, board, 1)

print(result)