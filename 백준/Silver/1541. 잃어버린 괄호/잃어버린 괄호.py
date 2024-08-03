import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(len(self.stack) - 1)


expressions = []
number = 0
for c in sys.stdin.readline().strip():
    if str.isdigit(c):
        number = number * 10 + int(c)

    elif c == '-':
        expressions.append(number)
        expressions.append('-')
        number = 0

    elif c == '+':
        expressions.append(number)
        expressions.append('+')
        number = 0

expressions.append(number)

stack = Stack()
i = 0
while len(expressions) > i:
    expression = expressions[i]
    if expression == '+':
        a = stack.pop()
        b = expressions[i + 1]
        stack.push(a + b)
        i += 1

    elif expression == '-':
        pass

    else:
        stack.push(expression)

    i += 1

result = stack.stack[0]
for number in stack.stack[1:]:
    result -= number

print(result)
