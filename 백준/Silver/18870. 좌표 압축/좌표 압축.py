import sys
INDEX = 0
VALUE = 1

N = int(sys.stdin.readline().strip())

coors = list(sys.stdin.readline().strip().split())
results = [None for _ in range(N)]

temp = []
for i, coor in enumerate(coors):
    temp.append((i, int(coor)))

coors = temp
coors.sort(key=lambda coor : coor[1])

rank = 0
compressed_coor = {}
for coor in coors:
    try:
        value = compressed_coor[coor[VALUE]]
    except KeyError:
        value = rank
        compressed_coor[coor[VALUE]] = rank
        rank += 1

    results[coor[INDEX]] = value

for result in results:
    print(result, end=" ")
