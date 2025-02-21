import sys


def postfix(exp):
    stack = []
    result = ''
    for x in exp:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] in ['*', '/']):
                result += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and (stack[-1] != '('):
                result += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and (stack[-1] != '('):
                result += stack.pop()
            stack.pop()
        else:
            result += x
    while stack:
        result += stack.pop()
    return result

s = sys.stdin.readline().strip()
print(postfix(s))
