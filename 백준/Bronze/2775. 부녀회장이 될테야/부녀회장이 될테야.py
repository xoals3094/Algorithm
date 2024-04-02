global before_floor


def in_room(room_number: int) -> int:
    return sum(before_floor[:room_number])


def count_room_members(n: int) -> list:
    members = []
    for room_number in range(1, n + 1):
        members.append(in_room(room_number))

    return members


def run():
    global before_floor
    k = int(input(''))
    n = int(input(''))
    before_floor = list(range(1, n + 1))
    for floor in range(1, k + 1):
        before_floor = count_room_members(n)

    print(before_floor[n-1])


T = int(input(''))
for _ in range(T):
    run()

