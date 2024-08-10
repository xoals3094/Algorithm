import sys

FRONT = 1
BACK = -1

T = int(sys.stdin.readline().strip())


class AC:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())
        self.array = []
        string = sys.stdin.readline().strip()
        if self.n > 0:
            self._get_array(string)
        self.direction = FRONT

    def _get_array(self, string):
        i = 0
        length = len(string)
        digit = 0
        while i < length:
            if string[i].isdigit():
                digit = digit * 10 + int(string[i])
            elif string[i] == ',' or string[i] == ']':
                self.array.append(digit)
                digit = 0
            i += 1

    def R(self):
        self.direction *= -1

    def D(self):
        if self.n == 0:
            raise Exception

        if self.direction == FRONT:
            self.array.pop(0)
        else:
            self.array.pop(-1)

        self.n -= 1

    def print(self):
        if self.direction == BACK:
            self.array.reverse()

        string = '['
        for i, x in enumerate(self.array):
            string += str(x)
            if i < self.n - 1:
                string += ','
        string += ']'
        print(string)


def command():
    func = sys.stdin.readline().strip()

    ac = AC()
    for f in func:
        if f == 'R':
            ac.R()

        elif f == 'D':
            try:
                ac.D()
            except Exception:
                print('error')
                return

    ac.print()


for _ in range(T):
    command()
