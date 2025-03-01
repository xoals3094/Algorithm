import sys

string = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()

stack = []
for c in string:
    stack.append(c)
    if len(stack) < len(boom):
        continue
    if stack[-1] == boom[-1] and ''.join(stack[len(stack) - len(boom):]) == boom:
        for _ in range(len(boom)):
            stack.pop()

print(''.join(stack) if len(stack) > 0 else 'FRULA')