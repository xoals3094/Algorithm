import sys

all_S = {}
for x in range(1, 20 + 1):
    all_S[str(x)] = True

empty_S = {}
for x in range(1, 20 + 1):
    empty_S[str(x)] = False


class Set:
    def __init__(self):
        self.S = empty_S.copy()

    def add(self, x):
        self.S[x] = True

    def remove(self, x):
        self.S[x] = False

    def check(self, x):
        if self.S[x]:
            print(1)
            return
        print(0)

    def toggle(self, x):
        if self.S[x]:
            self.S[x] = False
            return
        self.S[x] = True

    def all(self):
        self.S = all_S.copy()

    def empty(self):
        self.S = empty_S.copy()


def execute(command: str):
    if 'add' in command:
        _, x = command.split()
        s.add(x)

    elif 'remove' in command:
        _, x = command.split()
        s.remove(x)

    elif 'check' in command:
        _, x = command.split()
        s.check(x)

    elif 'toggle' in command:
        _, x = command.split()
        s.toggle(x)

    elif 'all' == command:
        s.all()

    elif 'empty' == command:
        s.empty()


m = int(sys.stdin.readline())

s = Set()

for _ in range(m):
    command = sys.stdin.readline().strip()
    execute(command)

