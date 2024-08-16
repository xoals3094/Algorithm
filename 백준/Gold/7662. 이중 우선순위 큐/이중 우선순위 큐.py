import sys
import heapq

T = int(sys.stdin.readline().strip())


def q():
    min_heap = []
    max_heap = []

    k = int(sys.stdin.readline().strip())
    nums = {}
    for _ in range(k):
        c, n = sys.stdin.readline().strip().split()
        if c == 'I':
            n = int(n)
            if n in nums:
                nums[n] += 1
            else:
                nums[n] = 1

            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)

        elif c == 'D':
            if n == '-1':
                while len(min_heap) > 0:
                    n = heapq.heappop(min_heap)
                    if nums[n] > 0:
                        nums[n] -= 1
                        break

            elif n == '1':
                while len(max_heap) > 0:
                    n = -heapq.heappop(max_heap)
                    if nums[n] > 0:
                        nums[n] -= 1
                        break

    queue = []
    for key, value in nums.items():
        if value > 0:
            queue.append(key)

    if len(queue) == 0:
        print('EMPTY')
        return

    print(max(queue), min(queue))


for _ in range(T):
    q()
