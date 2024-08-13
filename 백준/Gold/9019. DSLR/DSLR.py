import sys
MAX = 10000
T = int(sys.stdin.readline().strip())


class Register:
    def __init__(self, value):
        self.value = value

    def D(self):
        value = self.value
        value *= 2
        if value >= MAX:
            value %= MAX
        return value

    def S(self):
        value = self.value
        value -= 1
        if value < 0:
            value = MAX - 1

        return value

    def L(self):
        digit = []
        value = self.value
        while value > 0:
            digit.append(value % 10)
            value = value // 10

        if len(digit) < 4:
            digit = digit + [0] * (4 - len(digit))

        d1, d2, d3, d4 = digit

        value = ((d3 * 10 + d2) * 10 + d1) * 10 + d4

        return value

    def R(self):
        digit = []
        value = self.value
        while value > 0:
            digit.append(value % 10)
            value = value // 10

        if len(digit) < 4:
            digit = digit + [0] * (4 - len(digit))

        d1, d2, d3, d4 = digit
        value = ((d1 * 10 + d4) * 10 + d3) * 10 + d2
        return value


def get_result(visit, A, B):
    start = B
    result = []
    while start != A:
        end = start
        start = visit[start]
        register = Register(start)
        if register.D() == end:
            result.append('D')
        elif register.S() == end:
            result.append('S')
        elif register.L() == end:
            result.append('L')
        elif register.R() == end:
            result.append('R')

    result.reverse()

    return ''.join(result)


def DSLR():
    A, B = list(map(int, sys.stdin.readline().strip().split()))
    visit = [-1 for _ in range(MAX)]

    visit[A] = A
    q = [A]
    while len(q) > 0:
        temp = []
        for value in q:
            if value == B:
                return get_result(visit, A, B)

            register = Register(value)
            d = register.D()
            if visit[d] == -1:
                temp.append(d)
                visit[d] = value

            s = register.S()
            if visit[s] == -1:
                temp.append(s)
                visit[s] = value

            l = register.L()
            if visit[l] == -1:
                temp.append(l)
                visit[l] = value

            r = register.R()
            if visit[r] == -1:
                temp.append(r)
                visit[r] = value

        q = temp


for _ in range(T):
    print(DSLR())
