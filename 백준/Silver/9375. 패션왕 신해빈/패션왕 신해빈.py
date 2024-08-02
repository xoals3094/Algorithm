import sys

T = int(sys.stdin.readline().strip())


def fashion_king():
    wardrobe = {}
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        name, category = sys.stdin.readline().strip().split()
        try:
            wardrobe[category] += 1
        except KeyError:
            wardrobe[category] = 2

    case = 1
    for count in wardrobe.values():
        case *= count

    print(case - 1)


for _ in range(T):
    fashion_king()
