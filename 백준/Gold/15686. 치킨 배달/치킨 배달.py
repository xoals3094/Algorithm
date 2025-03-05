import sys

INF = int(1e9)
X = 0
Y = 1


N, M = map(int, sys.stdin.readline().strip().split())
graph = [sys.stdin.readline().strip().split() for _ in range(N)]

shops = []
houses = []

for y in range(N):
    for x in range(N):
        if graph[y][x] == '2':
            shops.append((x, y))
        elif graph[y][x] == '1':
            houses.append((x, y))

distance = [[INF for _ in range(len(houses))] for _ in range(len(shops))]
for shop_number, shop in enumerate(shops):
    for house_number, house in enumerate(houses):
        distance[shop_number][house_number] = abs(shop[X] - house[X]) + abs(shop[Y] - house[Y])

result = INF
def bt(n, selected):
    if len(selected) == M:
        global result

        chicken_distance = 0
        for house_number in range(len(houses)):
            shortest = INF
            for shop_number in selected:
                shortest = min(shortest, distance[shop_number][house_number])
            chicken_distance += shortest

        result = min(result, chicken_distance)
        return

    for i in range(n, len(shops)):
        bt(i + 1, selected + [i])


for i, shop in enumerate(shops):
    bt(i, [])
print(result)

