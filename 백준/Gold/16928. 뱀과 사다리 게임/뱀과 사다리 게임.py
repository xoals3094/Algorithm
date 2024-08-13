import sys

N, M = map(int, sys.stdin.readline().strip().split())

ladder_snake = {}
for _ in range(N + M):
    start, end = map(int, sys.stdin.readline().strip().split())
    ladder_snake[start] = end

visit = [False for _ in range(100 + 1)]

dice = (1, 2, 3, 4, 5, 6)


def game():
    q = [1]
    count = 0
    while len(q) > 0:
        temp = []
        for location in q:
            if location == 100:
                return count

            for number in dice:
                if location + number <= 100 and not visit[location + number]:
                    try:
                        end = ladder_snake[location + number]
                    except KeyError:
                        visit[location + number] = True
                        temp.append(location + number)
                    else:
                        visit[location + number] = True
                        visit[end] = True
                        temp.append(end)

        q = temp
        count += 1


print(game())
