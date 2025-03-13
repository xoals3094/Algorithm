import sys

K, N = map(int, sys.stdin.readline().strip().split())
lan_list = [int(sys.stdin.readline().strip()) for _ in range(K)]

def binary_search():
    lan = max(lan_list)
    result = 1

    start = 1
    end = lan
    while start <= end:
        center = (start + end) // 2
        count = 0
        for l in lan_list:
            count += l // center

        if count >= N:
            result = max(result, center)
            start = center + 1
        else:
            end = center - 1

    return result

print(binary_search())