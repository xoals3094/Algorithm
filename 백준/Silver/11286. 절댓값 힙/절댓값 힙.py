import sys

MAX = 100000


class Heap:
    def __init__(self):
        self.heap = [0 for _ in range(MAX + 1)]
        self.last = 0

    def insert(self, item):
        self.last += 1
        self.heap[self.last] = item
        i = self.last
        while i != 0 and abs(self.heap[i // 2]) >= abs(self.heap[i]):
            if abs(self.heap[i // 2]) == abs(self.heap[i]):
                if self.heap[i // 2] < self.heap[i]:
                    break
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    def remove(self) -> int:
        if self.last == 0:
            return 0

        item = self.heap[1]

        self.heap[1] = self.heap[self.last]
        self.heap[self.last] = 0
        self.last -= 1

        i = 1
        while i * 2 + 1 <= self.last:
            child = self._get_smaller(i)
            if child == i:
                break

            temp = self.heap[i]
            self.heap[i] = self.heap[child]
            self.heap[child] = temp
            i = child

        return item

    def _get_smaller(self, parent):
        target = parent
        if abs(self.heap[target]) >= abs(self.heap[parent * 2]):
            if abs(self.heap[target]) == abs(self.heap[parent * 2]):
                if self.heap[target] > self.heap[parent * 2]:
                    target = parent * 2
            else:
                target = parent * 2

        if abs(self.heap[target]) >= abs(self.heap[parent * 2 + 1]):
            if abs(self.heap[target]) == abs(self.heap[parent * 2 + 1]):
                if self.heap[target] > self.heap[parent * 2 + 1]:
                    target = parent * 2 + 1
            else:
                target = parent * 2 + 1

        return target


N = int(sys.stdin.readline().strip())
h = Heap()

for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print(h.remove())
    else:
        h.insert(n)
