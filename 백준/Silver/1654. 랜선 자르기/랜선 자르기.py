import sys
k, n = map(lambda x: int(x), sys.stdin.readline().split(' '))

lan_list = []
for _ in range(k):
    lan_list.append(int(sys.stdin.readline()))


def count_max_cutting_lan(cm: int):
    lan_count = 0
    for lan in lan_list:
        lan_count += lan // cm
    return lan_count


min_lan = 1
max_lan = max(lan_list)
while min_lan + 1 < max_lan:
    mid_lan = (min_lan + max_lan) // 2
    if count_max_cutting_lan(mid_lan) < n:
        max_lan = mid_lan
    else:
        min_lan = mid_lan
if count_max_cutting_lan(max_lan) >= n:
    print(max_lan)
else:
    print(min_lan)
