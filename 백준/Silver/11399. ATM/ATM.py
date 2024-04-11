import sys


n = int(sys.stdin.readline().strip())
p_list = list(map(int, sys.stdin.readline().strip().split()))

p_list.sort()

result = []
time = 0
for p in p_list:
    time += p
    result.append(time)

print(sum(result))